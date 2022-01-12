# Generated by Django 4.0 on 2022-01-12 16:49

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usersapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(
                default=uuid.UUID("7aad3cfd-6eda-4dd3-a672-61eba718666c"), primary_key=True, serialize=False
            ),
        ),
    ]
