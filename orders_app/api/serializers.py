from rest_framework import serializers
from orders_app.models import Orders
from offers_app.models import OfferDetails,Offers
from django.contrib.auth.models import User

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields='__all__'


    
class CreateOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['customer_user','business_user','title','revisions','delivery_time_in_days','price','features','offer_type','status','created_at','updated_at']

    def arrange_data(self,data,offer_detail,offer,customer_user,business_user):
        data.pop('offer_detail_id',[])
        data['customer_user'] = customer_user
        data['business_user'] = business_user
        data['title'] = offer_detail.title
        data['revisions'] = offer_detail.revisions
        data['delivery_time_in_days'] = offer_detail.delivery_time_in_days
        data['price'] = offer_detail.price
        data['features'] = offer_detail.features
        data['offer_type'] = offer_detail.offer_type

        return data


    def to_internal_value(self, data):
        request_data=self.initial_data
        offer_detail_id =request_data.get('offer_detail_id')
        customer_user=self.context['request'].user
        if not offer_detail_id:
            raise serializers.ValidationError({"offer_detail_id":"this field is required"})
        
        try:
            offer_detail=OfferDetails.objects.get(pk=offer_detail_id)
            offer=Offers.objects.get(pk=offer_detail.offer_id)
            business_user = User.objects.get(pk=offer.user_id)
        except OfferDetails.DoesNotExist:
            raise serializers.ValidationError({"offer_detail_id": "Invalid OfferDetails ID"})
        
        validated_data=self.arrange_data(data,offer_detail,offer,customer_user,business_user)
        print(validated_data)
        return validated_data

    def create(self, validated_data):
        return Orders.objects.create(**validated_data)
