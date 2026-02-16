from django.contrib import admin
from routing.models import Country,Network,Connectors,Routing
# Register your models here.
admin.site.register(Country)
admin.site.register(Network)
admin.site.register(Connectors)
admin.site.register(Routing)