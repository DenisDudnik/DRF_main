# Generated by Django 4.0 on 2022-01-12 18:38

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usersapp", "0003_alter_user_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]