from django.db import models

# Create your models here.
class SiteLikes(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

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
    tags = models.ManyToManyField(Tag, blank=True, through="TagsCareer")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.WorkSpace

class TagsCareer(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    joined_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag.name
