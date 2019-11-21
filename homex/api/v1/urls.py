from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import XXXViewSet

router = DefaultRouter()
router.register("xxx", XXXViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
