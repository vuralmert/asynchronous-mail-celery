from django.http import HttpResponse
from .tasks import schedule_mail_func
from django.views import View
from django.db.models import Q
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
from .serializers import SendMailSerializer
from django.core.files.base import ContentFile
from django.conf import settings
from .models import SentMail, Media
from .serializers import SentMailSerializer
from django.core.files.uploadedfile import InMemoryUploadedFile
import requests
import os


def schedule_mail(request):
    schedule_mail_func.delay()
    return HttpResponse("Mail scheduled")


class MailFormView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mail_form.html')


class SendMailView(GenericAPIView):
    serializer_class = SendMailSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            to_emails = [email.strip() for email in serializer.validated_data['to'].split(',')]
            subject = serializer.validated_data['subject']
            body = serializer.validated_data['body']
            cc_emails = [email.strip() for email in serializer.validated_data.get('cc', '').split(',') if email.strip()]
            attachments = serializer.validated_data.get('attachment', [])

            # Sending mail
            self.send_mail(to_emails, subject, body, cc_emails, attachments)

            # Storing mail
            sent_mail = SentMail(to=serializer.validated_data['to'],
                                 subject=subject,
                                 body=body,
                                 cc=serializer.validated_data.get('cc', ''),
                                 attachment=','.join(attachments))
            sent_mail.save()

            return Response({'message': 'Mail sent.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_mail(self, to_emails, subject, body, cc_emails, attachments):
        email = EmailMessage(subject, body, to=to_emails, cc=cc_emails)

        for attachment_url in attachments:
            media = self.download_attachment(attachment_url)
            if media is not None:
                if isinstance(media.file, InMemoryUploadedFile):
                    file_size_in_bytes = media.file.size
                    file_size_in_mb = file_size_in_bytes / (1024 * 1024)
                    if file_size_in_mb > 5:
                        continue

                email.attach(media.filename, media.file.read())

        email.send(fail_silently=True)

    def download_attachment(self, attachment_url):
        try:
            response = requests.get(attachment_url)
            response.raise_for_status()

            filename = os.path.basename(attachment_url)

            with open(os.path.join(settings.MEDIA_ROOT, 'attachments', filename), 'wb') as f:
                f.write(response.content)

            media = Media.objects.create(filename=filename, file='attachments/' + filename)
            media.save()

            return media
        except requests.exceptions.RequestException as e:
            print(f"Error while downloading attachments: {e}")
            return None


class SentMailListView(APIView):
    def get(self, request):
        queryset = self.get_queryset()

        serializer = SentMailSerializer(queryset, many=True)
        return Response({'mails': serializer.data}, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = SentMail.objects.all()

        # Filter by 'to' email address
        to_email = self.request.query_params.get('to')
        if to_email:
            queryset = queryset.filter(to__icontains=to_email)

        # Filter by 'subject'
        subject = self.request.query_params.get('subject')
        if subject:
            queryset = queryset.filter(subject__icontains=subject)

        # Order by a specific field
        order_by = self.request.query_params.get('order_by')
        if order_by:
            queryset = queryset.order_by(order_by)

        # Search by 'body' and 'subject' fields
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(body__icontains=search) | queryset.filter(subject__icontains=search)

        return queryset
