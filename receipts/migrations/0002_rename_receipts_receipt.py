# Generated by Django 4.2 on 2023-04-19 22:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("receipts", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Receipts",
            new_name="Receipt",
        ),
    ]
