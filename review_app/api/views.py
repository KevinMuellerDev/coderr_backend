from django.shortcuts import render
from rest_framework import viewsets
from review_app.models import Review
from review_app.api.serializers import ReviewsSerializer

# Create your views here.
class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class=ReviewsSerializer