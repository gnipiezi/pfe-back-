from django.db.models import Q
from rest_framework import viewsets
from housing.models import Apartment, Ticket, Profile
from housing.serializers import ApartmentSerializer, TicketSerializer, ProfileSerializer


class ApartmentViewSet(viewsets.ModelViewSet):

    serializer_class = ApartmentSerializer

    def get_queryset(self):
        return Apartment.objects.filter(Q(owner=self.request.user) | Q(site__owner=self.request.user))


class TicketViewSet(viewsets.ModelViewSet):

    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.filter(owner=self.request.user)


class ProfileViewSet(viewsets.ModelViewSet):

    serializer_class = ProfileSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Profile.objects.all()

        return Profile.objects.filter(owner=self.request.user)
