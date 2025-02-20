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
        review_count = 0
        average_rating = 0
        business_profile_count = 0
        offer_count = 0
        
        review_count = Review.objects.all().count()
        if review_count > 0:
            average_rating = (Review.objects.aggregate(Sum('rating'))['rating__sum'])/review_count
        else:
            review_count = 0
        business_profile_count = Profile.objects.filter(type='business').count()
        offer_count = Offers.objects.all().count()

        print(review_count)

        return Response({
            "review_count":review_count,
            "average_rating":average_rating,
            "business_profile_count":business_profile_count,
            "offer_count":offer_count
            },status.HTTP_200_OK)