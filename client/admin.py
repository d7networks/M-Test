from django.contrib import admin
from client.models import Client, Instance, Smsc


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('partner', 'instance', 'user_name', 'default_smsc')
    search_fields = ('partner', 'user_name')
    list_filter = ('user_name', 'partner')


@admin.register(Instance)
class ClientAdmin(admin.ModelAdmin):
    list_display = ()


@admin.register(Smsc)
class ClientAdmin(admin.ModelAdmin):
    list_display = ()