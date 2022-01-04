from django.contrib.auth.models import User
from rest_framework import serializers

from housing.models import Apartment, Ticket, Profile
from sensor.serializers import SensorSerializer


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "owner", "apartment", "description", "created_date", "status"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "address"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["profile"]

    profile = ProfileSerializer(many=True)


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ["id", "owner", "site", "address", "created_date", "last_updated", "sensors"]

    sensors = SensorSerializer(many=True)
    owner = UserSerializer()
