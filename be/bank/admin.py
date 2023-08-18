from django.contrib import admin
from .models import CardType, Bank, Card
# Register your models here.

admin.site.register(CardType)
admin.site.register(Bank)
admin.site.register(Card)