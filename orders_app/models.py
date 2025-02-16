from django.db import models
from userprofile_app.models import Profile

# Create your models here.
# Beispiel Modelstruktur Orders get
#   {
#     "id": 1,
#     "customer_user": 1,
#     "business_user": 2,
#     "title": "Logo Design",
#     "revisions": 3,
#     "delivery_time_in_days": 5,
#     "price": 150.00,
#     "features": ["Logo Design", "Visitenkarten"],
#     "offer_type": "basic",
#     "status": "in_progress",
#     "created_at": "2024-09-29T10:00:00Z",
#     "updated_at": "2024-09-30T12:00:00Z"
#   }

class Orders(models.Model):
    TYPES_CHOICE={
        'basic':'basic',
        'standard':'standard',
        'premium':'premium'
    }
    STATUS_CHOICE={
        'in_progress':'in_progress',
        'completed':'completed',
        'cancelled':'cancelled'
    }
    customer_user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    business_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=False)
    revisions  =models.IntegerField(null=False)
    delivery_time_in_days = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    features = models.JSONField(default=dict,null=False,blank=False)
    offer_type = models.CharField(choices=TYPES_CHOICE)
    status = models.CharField(choices=STATUS_CHOICE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)