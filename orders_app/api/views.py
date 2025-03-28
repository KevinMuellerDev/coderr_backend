from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from orders_app.models import Orders
from orders_app.api.serializers import OrdersSerializer,CreateOrdersSerializer
from orders_app.api.permissions import IsBusinessOwner,IsOwnerOrder


class OrdersViewset(viewsets.ModelViewSet):
    queryset=None
    serializer_class=OrdersSerializer
    permission_classes=[IsOwnerOrder]


    def get_queryset(self):
        """Nur Bestellungen des angemeldeten Business-Users abrufen"""
        if self.request.user.is_authenticated:
            return Orders.objects.filter(business_user=self.request.user)
        return Orders.objects.none() 

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
    
class OrderCount(APIView):
    permission_classes=[IsBusinessOwner]

    def get(self,request,business_user_id):
        count = 0
        count = Orders.objects.filter(business_user_id = business_user_id, status="in_progress").count()
        return Response({"order_count":count},status.HTTP_200_OK)
    
class OrderCompletedCount(APIView):
    permission_classes = [IsBusinessOwner]

    def get(self,request,business_user_id):
        count = Orders.objects.filter(business_user_id=business_user_id, status="completed").count()
        return Response({"completed_order_count":count},status.HTTP_200_OK)