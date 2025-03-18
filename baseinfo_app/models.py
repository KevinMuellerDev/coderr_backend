from django.db import models

# Create your models here.
class BaseInfo(models.Model):
    review_count = models.IntegerField()
    average_rating = models.FloatField()
    business_profile_count=models.IntegerField()
    offer_count=models.IntegerField()