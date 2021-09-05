from django.contrib import admin
from .models import SiteLikes, Career, Tag, TagsCareer, LoginLogging

class TagsCareerInline(admin.TabularInline):
    model = TagsCareer
    extra = 1

class CareerAdmin(admin.ModelAdmin):
    inlines = (TagsCareerInline,)


admin.site.register(TagsCareer)
admin.site.register(SiteLikes)
admin.site.register(Career, CareerAdmin)
admin.site.register(Tag)
admin.site.register(LoginLogging)
