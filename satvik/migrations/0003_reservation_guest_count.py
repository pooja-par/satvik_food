# Generated by Django 4.2.16 on 2024-09-15 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satvik', '0002_remove_reservation_guest_count_reservation_excerpt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='guest_count',
            field=models.IntegerField(default=1),
        ),
    ]
