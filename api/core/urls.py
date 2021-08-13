from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LikesViewSet, CareerViewSet, TagViewSet

router = DefaultRouter()
router.register(r"sitelikes", LikesViewSet, basename='SiteLikes')
router.register(r"tags", TagViewSet, basename='Tag')
router.register(r"career", CareerViewSet, basename='Career')

urlpatterns = [path("", include(router.urls))]
