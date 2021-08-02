from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LikesViewSet

router = DefaultRouter()
router.register(r'sitelikes', LikesViewSet)

urlpatterns = [
    path("", include(router.urls))
]
