from rest_framework import serializers

from .models import SiteLikes, Career, Tag
from django.contrib.auth.models import User

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteLikes
        fields = ("__all__")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = (
            "id",
            "WorkSpace",
            "website",
            "content",
            "StartWork",
            "EndWork",
            "tags",
            "created_at",
            "updated_at",
        )
        depth = 1

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password"
        )
