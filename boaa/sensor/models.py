from django.db import models
from housing.models import Apartment


SensorType = [
    ("WMZ_Arbeit", "WMZ_Arbeit"),
    ("WMZ_Kubikmeter", "WMZ_Kubikmeter"),
    ("WMZ_akt_Durchfluss", "WMZ_akt_Durchfluss"),
    ("WMZ_Leistung", "WMZ_Leistung"),
    ("WMZ_VL_Temp", "WMZ_VL_Temp"),
    ("WMZ_RL_Temp", "WMZ_RL_Temp"),
    ("WMZ_Spreizung", "WMZ_Spreizung"),
    ("GasZ", "GasZ"),
    ("StromZ", "StromZ"),
    ("WasserZ", "WasserZ")
]


class Sensor(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.PROTECT, related_name="sensors")
    sensor_types = models.CharField(max_length=128)
    uid = models.UUIDField()


class AggregatedSensorReading(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_created=True)


class SensorReading(models.Model):
    owner = models.ForeignKey(AggregatedSensorReading, on_delete=models.CASCADE, related_name="sensor_reading")
    sensor_type = models.CharField(choices=SensorType, max_length=18)
    value = models.FloatField()
