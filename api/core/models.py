from django.db import models

# Create your models here.
class SiteLikes(models.Model):
    love = models.IntegerField(null=True, blank=True)