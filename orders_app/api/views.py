from rest_framework import viewsets,status
from rest_framework.response import Response
from orders_app.models import Orders
from orders_app.api.serializers import OrdersSerializer,CreateOrdersSerializer


class OrdersViewset(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class=OrdersSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return OrdersSerializer
        elif self.request.method=="PATCH":
            return OrdersSerializer
        else:
            return CreateOrdersSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(
                {},
                status=status.HTTP_202_ACCEPTED
            )