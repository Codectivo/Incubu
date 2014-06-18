from django.contrib import admin
from usuarios.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'user_account', 'pass_account', 'user')
    list_per_page = 100

admin.site.register(Account, AccountAdmin)
