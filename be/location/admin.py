from django.contrib import admin
from .models import Area, Province, District, Ward

# Register your models here.

admin.site.register(Area)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Ward)
