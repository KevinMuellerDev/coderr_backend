# Generated by Django 5.1.6 on 2025-02-11 08:13

import django.db.models.deletion
import userprofile_app.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('file', models.FileField(blank=True, upload_to=userprofile_app.models.user_directory_path)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('tel', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True, max_length=50)),
                ('working_hours', models.CharField(blank=True, max_length=50)),
                ('type', models.CharField(choices=[('business', 'business'), ('customer', 'customer')], max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
