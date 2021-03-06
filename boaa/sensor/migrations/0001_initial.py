# Generated by Django 3.2.5 on 2021-08-23 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AggregatedSensorReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='SensorReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_type', models.CharField(choices=[('WMZ_Arbeit', 'WMZ_Arbeit'), ('WMZ_Kubikmeter', 'WMZ_Kubikmeter'), ('WMZ_akt_Durchfluss', 'WMZ_akt_Durchfluss'), ('WMZ_Leistung', 'WMZ_Leistung'), ('WMZ_VL_Temp', 'WMZ_VL_Temp'), ('WMZ_RL_Temp', 'WMZ_RL_Temp'), ('WMZ_Spreizung', 'WMZ_Spreizung'), ('GasZ', 'GasZ'), ('StromZ', 'StromZ'), ('WasserZ', 'WasserZ')], max_length=18)),
                ('value', models.FloatField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor.aggregatedsensorreading')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField()),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='housing.apartment')),
                ('sensor_types', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='aggregatedsensorreading',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor.sensor'),
        ),
    ]
