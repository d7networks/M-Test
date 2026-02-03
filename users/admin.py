from django.contrib import admin
from django.contrib.auth.models import User


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_editable = ('is_staff',)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
