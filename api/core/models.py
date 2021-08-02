from django.db import models

# Create your models here.
class Names(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return "Recipe for {}".format(self.name)