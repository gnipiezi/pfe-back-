from django.urls import include, path
from rest_framework import routers
from sensor.viewsets import SensorViewSet, get_reading, get_readings

router = routers.DefaultRouter()
router.register(r'sensor', SensorViewSet, basename="sensor")

urlpatterns = [
    path('', include(router.urls)),
    path(r'reading/<int:pk>/', get_reading, name="get_reading"),
    path(r'readings/<str:pks>/', get_readings, name="get_readings"),
]
