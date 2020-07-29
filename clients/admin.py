from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'first_name',
        'last_name',
        'email',
        'phone',
        'balance'
    )
    list_display_links = (
        'id',
        'first_name',
        'last_name'
    )

admin.site.register(Client, ClientAdmin)
