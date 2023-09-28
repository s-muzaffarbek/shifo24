from django.db import models
from location_field.models.plain import PlainLocationField


class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WorkPlace(models.Model):
    name = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['name'], zoom=10, suffix='Tashkent')

    @property
    def latitude(self):
        if self.location:
            return float(self.location.split(',')[0])
        return None

    @property
    def longitude(self):
        if self.location:
            return float(self.location.split(',')[1])
        return None

    def __str__(self):
        return self.name
