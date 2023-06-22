from django.http import HttpResponse
from .tasks import send_mail_func, schedule_mail_func


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Test mail sent")


def schedule_mail(request):
    schedule_mail_func.delay()
    return HttpResponse("Mail scheduled")
