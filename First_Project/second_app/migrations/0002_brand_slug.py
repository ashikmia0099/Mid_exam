# Generated by Django 4.2.6 on 2024-01-01 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
