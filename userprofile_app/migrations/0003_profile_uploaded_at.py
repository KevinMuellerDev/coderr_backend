# Generated by Django 5.1.6 on 2025-02-14 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile_app', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='uploaded_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
