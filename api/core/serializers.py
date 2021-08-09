from rest_framework import serializers
from .models import SiteLikes, Career, Tag


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteLikes
        fields = ("id", "love")

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
            "updated_at"
        )
        depth = 1