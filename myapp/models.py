from django.db import models
from location_field.models.plain import PlainLocationField
# Create your models here.

class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WorkPlace(models.Model):
    name = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['name'], zoom=10, suffix='Tashkent')

    def __str__(self):
        return self.name

class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    specialties = models.ManyToManyField(Specialty)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    work_experience = models.TextField(max_length=25, null=True, blank=True)
    workplace = models.ManyToManyField(WorkPlace)
    appointment_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    start_working = models.TimeField(default='09:00')
    end_working = models.TimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

