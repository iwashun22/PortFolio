from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LikesViewSet, CareerViewSet, TagViewSet

router = DefaultRouter()
router.register(r"sitelikes", LikesViewSet)
router.register(r"tags", TagViewSet)
router.register(r"career", CareerViewSet)

urlpatterns = [path("", include(router.urls))]
