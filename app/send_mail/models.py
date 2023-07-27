from django.db import models
from django.contrib.auth import get_user_model


class SentMail(models.Model):
    to = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)
    body = models.TextField()
    cc = models.CharField(max_length=1000, blank=True)
    attachment = models.TextField(blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.to}"


def upload_path(instance, filename):
    return f'attachments/{filename}'


class Media(models.Model):
    filename = models.CharField(max_length=1000)
    file = models.FileField(upload_to=upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename


class StoredEmail(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    subject = models.CharField(max_length=64)
    message = models.TextField()
    from_email = models.EmailField()
    to_email = models.EmailField()
    cc_email = models.TextField(blank=True)
    attachment = models.FileField(upload_to='media/', blank=True)
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
