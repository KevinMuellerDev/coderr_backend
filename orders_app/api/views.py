from rest_framework import viewsets
from orders_app.models import Orders
from orders_app.api.serializers import OrdersSerializer,CreateOrdersSerializer


class OrdersViewset(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class=OrdersSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return OrdersSerializer
        else:
            return CreateOrdersSerializer