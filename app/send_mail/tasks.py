from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import EmailMessage
from app import settings
from .models import StoredEmail
from datetime import datetime
import random
import glob


@shared_task()
def schedule_mail_func():
    active_users = get_user_model().objects.filter(is_active=True)
    current_time = datetime.now().strftime("%H:%M")
    attachment_files = glob.glob(f"{settings.ATTACHMENT_DIR}/*.txt")

    for user in active_users:
        mail_subject = "Schedule Testing"
        message = f"Current time: {current_time}"
        to_email = user.email
        cc_email = ['vural.mvce@gmail.com']
        attachment_path = None

        if attachment_files:
            attachment_path = random.choice(attachment_files)

        email = EmailMessage(
            subject=mail_subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[to_email],
            cc=cc_email,
        )
        if attachment_path:
            email.attach_file(attachment_path)

        email.send(fail_silently=True)

        stored_email = StoredEmail(
            user=user,
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            to_email=to_email,
            cc_email=", ".join(cc_email),
            attachment=attachment_path,
        )
        stored_email.save()

    return "Scheduled mail sent"
