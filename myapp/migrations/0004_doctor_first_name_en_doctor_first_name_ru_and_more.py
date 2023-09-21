# Generated by Django 4.2.5 on 2023-09-21 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_specialty_name_en_specialty_name_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='first_name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='first_name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='first_name_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='last_name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='last_name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='last_name_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='work_experience_en',
            field=models.TextField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='work_experience_ru',
            field=models.TextField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='work_experience_uz',
            field=models.TextField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='workplace',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='workplace',
            name='name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='workplace',
            name='name_uz',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
