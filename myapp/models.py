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

class Doctor(models.Model):
    STATUS = (
        ('at_work', 'at work'),
        ('not_at_work', 'not at work'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    specialties = models.ManyToManyField(Specialty)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    work_experience = models.TextField(max_length=25, null=True, blank=True)
    workplace = models.ManyToManyField(WorkPlace)
    appointment_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    start_working = models.TimeField(default='09:00')
    end_working = models.TimeField()
    status = models.CharField(max_length=32, choices=STATUS, default="at_work")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"