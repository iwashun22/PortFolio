from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NamesViewSet

router = DefaultRouter()
router.register(r'names', NamesViewSet)

urlpatterns = [
    path("", include(router.urls))
]
