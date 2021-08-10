from django.db import models

# Create your models here.
class SiteLikes(models.Model):
    love = models.IntegerField(null=True, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Career(models.Model):
    WorkSpace = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    StartWork = models.DateField()
    EndWork = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
