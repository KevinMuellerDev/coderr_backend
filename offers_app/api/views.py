from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from offers_app.models import OfferDetails,Offers
from offers_app.api.serializers import OfferInputSerializer,OfferGetSerializer,OfferDetailsSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from offers_app.api.permissions import IsOwnerOrReadOnly
class OffersPagination(PageNumberPagination):
    page_size=6
    max_page_size=6


class OfferFilter(FilterSet):
    creator_id = CharFilter(field_name="user__id")
    max_delivery_time = CharFilter(field_name="min_delivery_time", lookup_expr='lte')

    class Meta:
        model = Offers
        fields = ['creator_id', 'user']

class OffersViewset(viewsets.ModelViewSet):
    queryset = Offers.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    pagination_class=OffersPagination
    filterset_class = OfferFilter
    ordering_fields = ['created_at', 'updated_at', 'title', 'min_price', 'min_delivery_time']
    search_fields = ['title', 'description']
    permission_classes=[IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OfferGetSerializer
        else:
            return OfferInputSerializer
    

class OfferDetailsViewset(viewsets.ModelViewSet):
    queryset = OfferDetails.objects.all()
    serializer_class=OfferDetailsSerializer

