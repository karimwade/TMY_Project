from django.db import models

# Create your models here.

class TMYParameter(models.Model):
    project_name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    technology = models.CharField(max_length=100)
    pv_description = models.CharField(max_length=100)
    pv_tilt = models.FloatField()
    pv_azimuth = models.FloatField()
    tracker_description = models.CharField(max_length=100)
    tracker_gcr = models.FloatField()
    tracker_axis_azimuth = models.FloatField()
    tracker_max_angle = models.FloatField()
    request_id = models.CharField(max_length=100)
    p50 = models.BooleanField()
    p75 = models.BooleanField()
    p90 = models.BooleanField()
    p10 = models.BooleanField()
    p99 = models.BooleanField()
    ambient_temperature = models.BooleanField()
    pm_2_5 = models.BooleanField()
    pm_10 = models.BooleanField()
    relative_humidity = models.BooleanField()
    precipitable_water = models.BooleanField()
    wind_direction = models.BooleanField()
    granularity = models.IntegerField()

    def __str__(self):
        return self.project_name
