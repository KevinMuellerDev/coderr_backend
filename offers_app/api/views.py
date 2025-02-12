from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from offers_app.models import OfferDetails,Offers
from offers_app.api.serializers import OfferInputSerializer,OfferGetSerializer,OfferDetailsSerializer


class OffersPagination(PageNumberPagination):
    page_size=6
    max_page_size=6

class OffersViewset(viewsets.ModelViewSet):
    queryset = Offers.objects.all()
    pagination_class=OffersPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OfferGetSerializer
        else:
            return OfferInputSerializer

class OfferDetailsViewset(viewsets.ModelViewSet):
    queryset = OfferDetails.objects.all()
    serializer_class=OfferDetailsSerializer

