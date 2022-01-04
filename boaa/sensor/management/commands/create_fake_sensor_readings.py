import datetime
import uuid
import random
from django.core.management.base import BaseCommand, CommandError
import numpy.random as nrandom
from housing.models import Apartment
from sensor.models import Sensor, AggregatedSensorReading, SensorReading, SensorType


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('num_sensors_per_apartment', default=5, type=int)

    def handle(self, *args, **options):
        num_sensors = options['num_sensors_per_apartment']
        for apartment in Apartment.objects.all():
            for _ in range(num_sensors):
                sensor_types = random.sample([t[0] for t in SensorType], k=5)
                sensor = Sensor.objects.create(
                    apartment=apartment,
                    uid=uuid.uuid4(),
                    sensor_types=sensor_types
                )

                date_list = [datetime.datetime.now() - datetime.timedelta(weeks=x) for x in range(1, 53)]
                value_list = nrandom.normal(random.randint(1, 100), size=(52, num_sensors))
                for date, values in zip(date_list, value_list):
                    agg = AggregatedSensorReading.objects.create(
                        sensor=sensor,
                        created_date=date
                    )
                    for sensor_type, value in zip(sensor_types, values):
                         SensorReading.objects.create(
                            owner=agg,
                            sensor_type=sensor_type,
                            value=value
                        )
            self.stdout.write(self.style.SUCCESS('Successfully created readings'))
