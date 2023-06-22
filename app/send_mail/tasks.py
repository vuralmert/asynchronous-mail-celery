from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail, EmailMessage
from app.app import settings
from datetime import datetime


@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Celery Testing"
        message = "This is a test message written by Mert v2"
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Test mail sent"


@shared_task()
def schedule_mail_func():
    users = get_user_model().objects.all()
    current_time = datetime.now().strftime("%H:%M")

    for user in users:
        mail_subject = "Schedule Testing"
        message = f"Current time: {current_time}"
        to_email = user.email
        cc_email = ['vural.mvce@gmail.com']

        email = EmailMessage(
            subject=mail_subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[to_email],
            cc=cc_email,
        )
        email.send(fail_silently=True)

    return "Scheduled mail sent"
