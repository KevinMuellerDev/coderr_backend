# Generated by Django 5.1.6 on 2025-02-12 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0005_offerdetails_feature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offerdetails',
            old_name='feature',
            new_name='features',
        ),
        migrations.DeleteModel(
            name='OfferFeature',
        ),
    ]
