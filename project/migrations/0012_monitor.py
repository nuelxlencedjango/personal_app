# Generated by Django 4.0.2 on 2023-06-26 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('capital', models.CharField(blank=True, max_length=50, null=True)),
                ('datetime', models.DateField(blank=True, max_length=50, null=True)),
                ('ip', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
