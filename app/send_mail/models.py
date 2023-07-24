from django.db import models


class StoredEmail(models.Model):
    subject = models.CharField(max_length=64)
    message = models.TextField()
    from_email = models.EmailField()
    to_email = models.EmailField()
    cc_email = models.TextField(blank=True)
    attachment = models.FileField(upload_to='media/', blank=True)
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
