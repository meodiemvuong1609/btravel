from django.db import models
from account.models import Account
# Create your models here.


class CardType(models.Model):
    title        = models.CharField(max_length=255)
    code         = models.CharField(max_length=255, unique=True) # VISA, ATM, MASTER
    created_at	 = models.DateTimeField(auto_now_add=True)
    updated_at	 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Bank(models.Model):
    title        = models.CharField(max_length=255)
    code         = models.CharField(max_length=255, unique=True)
    short_name   = models.CharField(max_length=255, null=True, blank=True, default=None)
    img_url      = models.CharField(max_length=255, null=True, blank=True, default=None)
    bin          = models.CharField(max_length=255, null=True, blank=True, default=None)
    swiftCode    = models.CharField(max_length=255, null=True, blank=True, default=None)
    created_at	 = models.DateTimeField(auto_now_add=True)
    updated_at	 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Card(models.Model):
    card_number     = models.CharField(max_length=255)
    full_name       = models.CharField(max_length=255, null=True, blank=True, default=None)
    status          = models.BooleanField(default=True, blank=True)
    card_type       = models.ForeignKey(CardType, on_delete=models.DO_NOTHING, blank=True)
    bank            = models.ForeignKey(Bank, on_delete=models.DO_NOTHING, blank=True)
    account         = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    created_at	    = models.DateTimeField(auto_now_add=True)
    updated_at	    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.card_number