from django.shortcuts import render
from rest_framework import viewsets
from review_app.models import Review
from review_app.api.serializers import ReviewsSerializer
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter


# Create your views here.
class ReviewFilter(FilterSet):
    business_user_id = CharFilter(field_name='business_user__id')
    reviewer_id=CharFilter(field_name='reviewer__id')

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class=ReviewsSerializer
    ordering_fields = ['']
    filterset_class = ReviewFilter
