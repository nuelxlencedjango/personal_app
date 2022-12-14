# Generated by Django 3.2 on 2022-06-14 14:34

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('functionality1', models.CharField(blank=True, max_length=200, null=True)),
                ('functionality2', models.CharField(blank=True, max_length=200, null=True)),
                ('functionality3', models.CharField(blank=True, max_length=200, null=True)),
                ('functionality4', models.CharField(blank=True, max_length=200, null=True)),
                ('functionality5', models.CharField(blank=True, max_length=200, null=True)),
                ('technology', models.CharField(blank=True, max_length=200, null=True)),
                ('img', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Property',
            },
        ),
    ]
