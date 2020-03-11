from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'makes', views.MakeViewSet)
router.register(r'models', views.ModelViewSet)
router.register(r'trims', views.TrimViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
