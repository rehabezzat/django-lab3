# Generated by Django 5.1 on 2024-08-23 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("track", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="track",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="track/images/"),
        ),
    ]
