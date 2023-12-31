# Generated by Django 4.2.5 on 2023-09-24 07:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0004_doctor_first_name_en_doctor_first_name_ru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message="Telefon raqamini to'g'ri ko'rsating, masalan: +998901234567", regex='^\\+998\\d{9}$')])),
                ('workplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.workplace')),
            ],
        ),
    ]
