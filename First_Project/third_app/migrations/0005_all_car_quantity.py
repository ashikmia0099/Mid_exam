# Generated by Django 4.2.6 on 2024-01-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third_app', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_car',
            name='Quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
