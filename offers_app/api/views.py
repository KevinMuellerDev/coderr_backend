from rest_framework import viewsets
from offers_app.models import OfferDetails,OfferFeature,Offers
from userprofile_app.api.serializers import ProfileSerializer
from offers_app.api.serializers import OfferSerializer,OfferFeatureSerializer,OfferDetailsSerializer


class OffersViewset(viewsets.ModelViewSet):
    queryset = Offers.objects.all()
    serializer_class = OfferSerializer

class OfferDetailsViewset(viewsets.ModelViewSet):
    queryset = OfferDetails.objects.all()
    serializer_class=OfferDetailsSerializer
