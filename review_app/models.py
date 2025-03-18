from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    RATING_CHOICE = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5
    }
    business_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business_user')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='review_user')
    rating = models.IntegerField(choices=RATING_CHOICE, null=False)
    description = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
