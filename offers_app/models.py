from django.db import models
from django.contrib.auth.models import User

def user_offer_directory_path(instance, filename):
    """
    Returns Filepath where instance provides the user.id and filename
    the name of provided data
    - `instance`: instance.user.id
    - `filename`: name of data
    """
    return f'offers/{instance.id}/{filename}'

# Create your models here.
class Offers(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=False,blank=False)
    image = models.FileField(upload_to=user_offer_directory_path, null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    min_price=models.FloatField(null=True)
    min_delivery_time = models.IntegerField(null=True,blank=True)

class OfferDetails(models.Model):
    TYPES_CHOICE={
        'basic':'basic',
        'standard':'standard',
        'premium':'premium'
    }
    offer=models.ForeignKey(Offers,on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    revisions=models.IntegerField()
    delivery_time_in_days=models.IntegerField()
    price=models.FloatField()
    offer_type=models.CharField(choices=TYPES_CHOICE,max_length=8)
    features=models.JSONField(default=dict)

    def __str__(self):
        return super().__str__()

    





