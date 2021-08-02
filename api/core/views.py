from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import NamesSerializer
from .models import Names

class NamesViewSet(viewsets.ModelViewSet):
    serializer_class = NamesSerializer
    queryset = Names.objects.all()
