from django.contrib import admin
from partner.models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'phone', 'account_type')
    search_fields = ('company_name', 'email')
    list_filter = ('account_type',)
