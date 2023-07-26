from django.urls import path
from . import views
from .views import SendMailView, MailFormView, SentMailListView

urlpatterns = [
    path('send_mail/', SendMailView.as_view(), name="send_mail"),
    path('mail_form/', MailFormView.as_view(), name="mail_form"),
    path('sent_mails/', SentMailListView.as_view(), name='sent_mails'),
    path('schedule_mail/', views.schedule_mail, name="schedule_mail"),
]
