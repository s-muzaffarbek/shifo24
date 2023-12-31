# Generated by Django 4.2.5 on 2023-09-28 09:41

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_delete_doctor'),
        ('users', '0009_alter_adminuser_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message="Telefon raqamini to'g'ri ko'rsating, masalan: +998901234567", regex='^\\+998\\d{9}$')])),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workplace', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admins', to='myapp.workplace')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('work_experience', models.TextField(blank=True, max_length=25, null=True)),
                ('appointment_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('start_working', models.TimeField(default='09:00')),
                ('end_working', models.TimeField()),
                ('status', models.CharField(choices=[('at_work', 'at work'), ('not_at_work', 'not at work')], default='at_work', max_length=32)),
                ('specialties', models.ManyToManyField(to='myapp.specialty')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workplace', models.ManyToManyField(related_name='doctors', to='myapp.workplace')),
            ],
        ),
        migrations.DeleteModel(
            name='AdminUser',
        ),
    ]
