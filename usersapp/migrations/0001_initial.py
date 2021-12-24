# Generated by Django 4.0 on 2021-12-24 14:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('birthday', models.DateField(blank=True)),
                ('uuid', models.UUIDField(default=uuid.UUID('239cadbc-6e8c-4bb3-a59d-95964675cf7e'), primary_key=True, serialize=False)),
            ],
        ),
    ]
