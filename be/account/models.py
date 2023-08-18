from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from account.custommanager import CustomUserManager
from location.models import Province, District, Ward, Area
import string, secrets

# Create your models here.

class Address(models.Model):
    title       = models.CharField(max_length=255)
    lat         = models.FloatField(null=True, blank=True, default=None)
    long        = models.FloatField(null=True, blank=True, default=None)
    area        = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    province    = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    district    = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    ward        = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    created_at	= models.DateTimeField(default=timezone.now)
    updated_at	= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
        
class System(models.Model):
    title        = models.CharField(max_length=255)
    code         = models.CharField(max_length=255, unique=True)
    created_at	 = models.DateTimeField(default=timezone.now)
    updated_at	 = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title or ''
    
class AccountType(models.Model):
    title               = models.CharField(max_length=255)
    code                = models.CharField(max_length=255, blank=True, null=True, default=None)
    description         = models.TextField(null=True, blank=True, default=None)
    settings            = models.JSONField(default=dict, blank=True)
    account_type_parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, default=None)
    system              = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    user_created        = models.ForeignKey("account.Account", on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name="user_created_account_type")
    created_at	        = models.DateTimeField(default=timezone.now)
    updated_at	        = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return self.title or ''


class Gender(models.Model):
    title        = models.CharField(max_length=255)
    code         = models.CharField(max_length=255, unique=True)
    created_at	 = models.DateTimeField(default=timezone.now)
    updated_at	 = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title or ''
    
class Account(AbstractUser):
    phone           = models.CharField(max_length=20, unique=True)
    email           = models.EmailField(max_length=50, blank=True, null=True, default=None)
    key_account     = models.CharField(max_length=255, default=None, blank=True, null=True)
    full_name       = models.CharField(max_length=50, null=True, blank=True)
    birthday        = models.DateField(null=True, blank=True, default=None)
    avatar          = models.ImageField(upload_to='account/avatar/', null=True, blank=True)
    tax_code        = models.CharField(max_length=255, null=True, blank=True, default=None)
    reward_points   = models.IntegerField(default=0, blank=True)
    settings        = models.JSONField(default=dict, blank=True)
    address         = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    gender          = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    account_type    = models.ForeignKey(AccountType, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    parent_account  = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, default=None)
    user_created    = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name="user_created_account")
    system          = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    created_at	    = models.DateTimeField(default=timezone.now)
    updated_at	    = models.DateTimeField(default=timezone.now)
    username        = None
    first_name      = None
    last_name       = None
    USERNAME_FIELD  = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone
