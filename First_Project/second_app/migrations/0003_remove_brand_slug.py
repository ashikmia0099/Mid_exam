# Generated by Django 4.2.6 on 2024-01-01 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0002_brand_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='slug',
        ),
    ]
