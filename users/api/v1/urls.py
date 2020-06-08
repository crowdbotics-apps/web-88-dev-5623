from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import WGWEtgrgtrtViewSet

router = DefaultRouter()
router.register("wgwetgrgtrt", WGWEtgrgtrtViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
