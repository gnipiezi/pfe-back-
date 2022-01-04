from rest_framework import serializers
from sensor.models import Sensor, SensorReading, AggregatedSensorReading


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ["apartment", "uid", "pk", "sensor_types"]


class SensorReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorReading
        fields = ["sensor_type", "value"]


class AggregatedSensorReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedSensorReading
        fields = ["sensor", "created_date", "sensor_reading"]

    sensor_reading = SensorReadingSerializer(many=True)
