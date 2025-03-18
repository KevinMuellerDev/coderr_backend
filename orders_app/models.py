from django.db import models
from django.contrib.auth.models import User


class Orders(models.Model):
    TYPES_CHOICE = {
        'basic': 'basic',
        'standard': 'standard',
        'premium': 'premium'
    }
    STATUS_CHOICE = {
        'in_progress': 'in_progress',
        'completed': 'completed',
        'cancelled': 'cancelled'
    }
    customer_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='customer_user_order')
    business_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='business_user_order')
    title = models.CharField(max_length=100, blank=False)
    revisions = models.IntegerField(null=False)
    delivery_time_in_days = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    features = models.JSONField(default=dict, null=False, blank=False)
    offer_type = models.CharField(choices=TYPES_CHOICE, max_length=20)
    status = models.CharField(choices=STATUS_CHOICE, max_length=20, default='in_progress')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
