from django.contrib import admin
from .models import Account

class accountsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'is_admin', 'last_login')

admin.site.register(Account, accountsAdmin)