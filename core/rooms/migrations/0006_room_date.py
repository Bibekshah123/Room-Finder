# Generated by Django 5.2.1 on 2025-06-11 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_alter_booking_booked_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
