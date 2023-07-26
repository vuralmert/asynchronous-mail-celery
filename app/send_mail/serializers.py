from rest_framework import serializers
from .models import SentMail


class SendMailSerializer(serializers.Serializer):
    to = serializers.CharField(help_text="Who to send mail to. Separate with commas for multiple emails.")
    subject = serializers.CharField(help_text="Mail subject")
    body = serializers.CharField(help_text="Mail body")
    cc = serializers.CharField(help_text="Emails to be added to CC. Separate with commas for multiple emails")
    attachment = serializers.ListField(child=serializers.URLField(), help_text="Additional links to be added (max 5MB)", required=False)


class SentMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentMail
        fields = '__all__'
