from django.shortcuts import render
from rest_framework import viewsets
from review_app.models import Review
from review_app.api.serializers import ReviewsSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter


# Create your views here.
class ReviewFilter(FilterSet):
    business_user_id = CharFilter(field_name='business_user__id')
    reviewer_id=CharFilter(field_name='reviewer__id')

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class=ReviewsSerializer
    filter_backends=[DjangoFilterBackend,OrderingFilter]
    ordering_fields = ['created_at','updated_at','rating']
    filterset_class = ReviewFilter
