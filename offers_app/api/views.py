from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from offers_app.models import OfferDetails,OfferFeature,Offers
from userprofile_app.api.serializers import ProfileSerializer
from offers_app.api.serializers import OfferSerializer,OfferFeatureSerializer,OfferDetailsSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class OffersViewset(viewsets.ModelViewSet):
    queryset = Offers.objects.all()
    serializer_class = OfferSerializer

class OfferDetailsViewset(viewsets.ModelViewSet):
    queryset = OfferDetails.objects.all()
    serializer_class=OfferDetailsSerializer

