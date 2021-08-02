from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import generics
from .serializers import LikeSerializer
from .models import SiteLikes

class LikesViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = SiteLikes.objects.all()