# Generated by Django 4.2.3 on 2025-02-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RideRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_km', models.FloatField()),
                ('traffic_level', models.CharField(choices=[('low', 'Low'), ('normal', 'Normal'), ('high', 'High')], max_length=10)),
                ('demand_level', models.CharField(choices=[('low', 'Low'), ('normal', 'Normal'), ('peak', 'Peak')], max_length=10)),
                ('calculated_fare', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
