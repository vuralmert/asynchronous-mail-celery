from django.contrib import admin
from .models import SentMail, Media, StoredEmail


class SentMailAdmin(admin.ModelAdmin):
    list_display = ('to', 'subject', 'sent_at')
    list_filter = ('sent_at',)
    search_fields = ('to', 'subject')


admin.site.register(SentMail, SentMailAdmin)


class MediaAdmin(admin.ModelAdmin):
    list_display = ('filename', 'uploaded_at')
    list_filter = ('uploaded_at',)


admin.site.register(Media, MediaAdmin)


class StoredEmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'message', 'to_email', 'sent_date')
    search_fields = ('subject', 'to_email')
    list_filter = ('sent_date',)
    readonly_fields = ('subject', 'message', 'from_email', 'to_email', 'cc_email', 'attachment', 'sent_date')


admin.site.register(StoredEmail, StoredEmailAdmin)
