import datetime

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from housing.models import Apartment
from sensor.models import Sensor, AggregatedSensorReading
from sensor.serializers import SensorSerializer, AggregatedSensorReadingSerializer


class SensorViewSet(viewsets.ModelViewSet):

    serializer_class = SensorSerializer

    def get_queryset(self):
        apartments = Apartment.objects.filter(owner=self.request.user)
        return Sensor.objects.filter(apartment__id__in=[apartment.id for apartment in apartments])


def has_apartment_permission(user, sensor: Sensor) -> bool:
        if user == sensor.apartment.owner:
            return True
        elif sensor.apartment.site is not None and user == sensor.apartment.site.owner:
            return True
        return False

@api_view(['GET'])
def get_reading(request, *args, **kwargs):
    pk = kwargs.pop("pk")
    end_date = request.query_params.get("end_date", datetime.datetime.now())
    start_date = request.query_params.get("start_date", datetime.datetime.now() - datetime.timedelta(days=365))

    sensor = get_object_or_404(Sensor, pk=pk)
    if not has_apartment_permission(request.user, sensor):
        raise PermissionError("Not enough permission to query the sensor.")

    aggregated = AggregatedSensorReading.objects.filter(sensor=sensor, created_date__range=(start_date, end_date))
    serialized = AggregatedSensorReadingSerializer(aggregated, many=True)
    return Response(serialized.data)


@api_view(['GET'])
def get_readings(request, *args, **kwargs):
    pks = kwargs.pop('pks').split(',')
    end_date = request.query_params.get("end_date", datetime.datetime.now())
    start_date = request.query_params.get("start_date", datetime.datetime.now() - datetime.timedelta(days=365))

    sensors = Sensor.objects.filter(pk__in=pks)
    is_owner = [has_apartment_permission(request.user, sensor) for sensor in sensors]

    if not all(is_owner):
        raise PermissionError("Not enough permission to query all sensors.")

    aggregated = AggregatedSensorReading.objects.filter(sensor_id__in=[sensor.pk for sensor in sensors], created_date__range=(start_date, end_date))
    serialized = AggregatedSensorReadingSerializer(aggregated, many=True)
    return Response(serialized.data)
