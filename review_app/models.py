from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#   {
#     "id": 1,
#     "business_user": 2, <= Id des Business Users
#     "reviewer": 3, <= Id des Bewerters(Customer und Business?)
#     "rating": 4,
#     "description": "Sehr professioneller Service.",
#     "created_at": "2023-10-30T10:00:00Z",
#     "updated_at": "2023-10-31T10:00:00Z"
#   },
#   {
#     "id": 2,
#     "business_user": 5,
#     "reviewer": 3,
#     "rating": 5,
#     "description": "Top Qualität und schnelle Lieferung!",
#     "created_at": "2023-09-20T10:00:00Z",
#     "updated_at": "2023-09-20T12:00:00Z"
#   }


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
