# Generated by Django 4.0.2 on 2023-06-26 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField(default=None)),
                ('date_visited', models.DateTimeField(auto_now_add=True)),
                ('visitDate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
