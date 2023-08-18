from django.db import models

# Create your models here.

class Area(models.Model):
    title       = models.CharField(max_length=255)
    code        = models.CharField(max_length=255)
    def __str__(self):
        return self.title
    
class Province(models.Model):
    title       = models.CharField(max_length=255)
    code        = models.CharField(max_length=255)
    area        = models.ForeignKey(Area, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class District(models.Model):
    title       = models.CharField(max_length=255)
    code        = models.CharField(max_length=255)
    province    = models.ForeignKey(Province, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class Ward(models.Model):
    title       = models.CharField(max_length=255)
    code        = models.CharField(max_length=255)
    district    = models.ForeignKey(District, on_delete=models.CASCADE)
    def __str__(self):
        return self.title