from django.contrib import admin
from account.models import Account, AccountType, Address, Gender, System

# Register your models here.
admin.site.register(Account)
admin.site.register(AccountType)
admin.site.register(Address)
admin.site.register(Gender)
admin.site.register(System)