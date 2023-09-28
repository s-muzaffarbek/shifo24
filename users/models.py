from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group, UserManager
from django.utils.translation import gettext as _
from myapp.models import WorkPlace, Specialty

phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Telefon raqamini to'g'ri ko'rsating, masalan: +998901234567",
)

class User(AbstractBaseUser):
    phone = models.CharField(
        validators=[phone_regex],
        max_length=15,
        unique=True,
    )
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    username = models.CharField(max_length=50, unique=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.get_username()

class Admin(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    workplace = models.OneToOneField(WorkPlace, on_delete=models.CASCADE, related_name='admins')


class Doctor(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    workplace = models.ManyToManyField(WorkPlace, related_name='doctors')
    STATUS = (
        ('at_work', 'at work'),
        ('not_at_work', 'not at work'),
    )
    specialties = models.ManyToManyField(Specialty)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    work_experience = models.TextField(max_length=25, null=True, blank=True)
    appointment_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    start_working = models.TimeField(default='09:00')
    end_working = models.TimeField()
    status = models.CharField(max_length=32, choices=STATUS, default="at_work")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class CustomUser(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)









