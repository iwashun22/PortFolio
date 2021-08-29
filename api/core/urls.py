from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LikesViewSet, CareerViewSet, TagViewSet, SignUpView, SignInView, LoginView

router = DefaultRouter()
router.register(r"register", SignUpView, basename='Register')
router.register(r"login", SignInView, basename='login')
router.register(r"me", LoginView, basename='auth')
router.register(r"sitelikes", LikesViewSet, basename='SiteLikes')
router.register(r"tags", TagViewSet, basename='Tag')
router.register(r"career", CareerViewSet, basename='Career')

urlpatterns = [
    path("", include(router.urls))
]
