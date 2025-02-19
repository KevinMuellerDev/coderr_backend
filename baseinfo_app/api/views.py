from rest_framework.views import APIView
from review_app.models import Review
from userprofile_app.models import Profile
from offers_app.models import Offers
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class BaseInfoView(APIView):
    permission_classes=[AllowAny]

    
    def get(self,request):
        review_count = Review.objects.all().count()
        average_rating = (Review.objects.aggregate(Sum('rating'))['rating__sum'])/review_count
        business_profile_count = Profile.objects.filter(type='business').count()
        offer_count = Offers.objects.all().count()

        return Response({
            "review_count:":review_count,
            "average_rating":average_rating,
            "business_profile_count":business_profile_count,
            "offer_count":offer_count
            },status.HTTP_200_OK)