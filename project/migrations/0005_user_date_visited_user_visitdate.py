# Generated by Django 4.0.2 on 2023-06-26 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_contactus_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_visited',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='visitDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
