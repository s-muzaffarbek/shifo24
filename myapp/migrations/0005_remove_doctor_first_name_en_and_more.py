# Generated by Django 4.2.5 on 2023-09-26 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_doctor_first_name_en_doctor_first_name_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='first_name_en',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='first_name_ru',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='first_name_uz',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='last_name_en',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='last_name_ru',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='last_name_uz',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='work_experience_en',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='work_experience_ru',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='work_experience_uz',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='name_uz',
        ),
        migrations.RemoveField(
            model_name='workplace',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='workplace',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='workplace',
            name='name_uz',
        ),
    ]