from django.contrib import admin
from routing.models import Routers, Country, Network, Connectors


@admin.register(Routers)
class RoutersAdmin(admin.ModelAdmin):
    list_display = ('partner', 'client')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ()


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ()


@admin.register(Connectors)
class ConnectorsAdmin(admin.ModelAdmin):
    list_display = ()