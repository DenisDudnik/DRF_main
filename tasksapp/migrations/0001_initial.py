# Generated by Django 4.0 on 2022-01-12 16:49

import uuid

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("usersapp", "0002_alter_user_uuid"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.UUID("6502baff-3e0c-4fc7-8e08-27f39c5d222b"), primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("repo_link", models.URLField(blank=True, null=True)),
                ("users", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="TODO",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.UUID("a6abebc3-c7ab-4eaa-8c2c-c6d3e06268b7"), primary_key=True, serialize=False
                    ),
                ),
                ("task_text", models.CharField(max_length=255)),
                ("date_created", models.DateTimeField(default=django.utils.timezone.now)),
                ("date_updated", models.DateTimeField(default=django.utils.timezone.now)),
                ("is_active", models.BooleanField(default=True)),
                ("created_by", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="usersapp.user")),
                ("project", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="tasksapp.project")),
            ],
        ),
    ]
