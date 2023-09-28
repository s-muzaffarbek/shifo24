# Generated by Django 4.2.5 on 2023-09-26 19:25

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_adminuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='phone',
            field=models.CharField(default=datetime.datetime(2023, 9, 26, 19, 25, 4, 532576, tzinfo=datetime.timezone.utc), max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message="Telefon raqamini to'g'ri ko'rsating, masalan: +998901234567", regex='^\\+998\\d{9}$')]),
            preserve_default=False,
        ),
    ]