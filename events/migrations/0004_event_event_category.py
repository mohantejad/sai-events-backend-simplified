# Generated by Django 5.1.7 on 2025-04-02 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0003_rename_location_event_city"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="event_category",
            field=models.CharField(
                choices=[
                    ("Music", "Music"),
                    ("Nightlife", "Nightlife"),
                    ("Performing & Visual Arts", "Arts"),
                    ("Holidays", "Holidays"),
                    ("Dating", "Dating"),
                    ("Hobbies", "Hobbies"),
                    ("Business", "Business"),
                    ("Food & Drink", "Food Drink"),
                ],
                default=None,
                max_length=255,
            ),
            preserve_default=False,
        ),
    ]
