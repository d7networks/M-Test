from django.contrib import admin

# Register your models here.
from .models import Network, Country, Connector

admin.site.register(Network)
admin.site.register(Country)
admin.site.register(Connector)