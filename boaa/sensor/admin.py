from django.contrib import admin
from sensor.models import Sensor, AggregatedSensorReading

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ["uid"]


@admin.register(AggregatedSensorReading)
class AggregatedSensorReadingAdmin(admin.ModelAdmin):
    list_display = ["sensor", "created_date"]
