from django.urls import include, path
from rest_framework import routers
from housing.viewsets import ApartmentViewSet, TicketViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register(r'apartment', ApartmentViewSet, basename="apartment")
router.register(r'ticket', TicketViewSet, basename="ticket")
router.register(r'profile', ProfileViewSet, basename="profile")

urlpatterns = [
    path('', include(router.urls)),
]
