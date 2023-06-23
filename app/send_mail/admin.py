from django.contrib import admin
from .models import StoredEmail


class StoredEmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'message', 'to_email', 'sent_date')
    search_fields = ('subject', 'to_email')
    list_filter = ('sent_date',)
    readonly_fields = ('subject', 'message', 'from_email', 'to_email', 'cc_email', 'attachment', 'sent_date')


admin.site.register(StoredEmail, StoredEmailAdmin)
