from rest_framework import serializers
from .models import SiteLikes


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteLikes
        fields = ("id", "love")
