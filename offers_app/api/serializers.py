from rest_framework import serializers
from offers_app.models import OfferDetails,Offers
from django.contrib.auth.models import User

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['first_name','last_name','username']

class OfferDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=OfferDetails
        fields=['id','title','revisions','delivery_time_in_days','price','features','offer_type']

    

class OfferDetailsLinkedSerializer(OfferDetailsSerializer,serializers.HyperlinkedModelSerializer):
     class Meta:
         model=OfferDetails
         fields=['id','url']


class OfferGetSerializer(serializers.ModelSerializer):
    user_details = UserDetailsSerializer(source='user',read_only=True)
    details = OfferDetailsLinkedSerializer(many=True,source='offerdetails_set')

    
    class Meta:
        model=Offers
        fields = ['id','user','title','description','created_at','updated_at','details','image','min_price','min_delivery_time','user_details']
        extra_kwargs={
            'image':{'required':False}
        }



class OfferInputSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True) 
    user_details = UserDetailsSerializer(source='user',read_only=True)
    details = OfferDetailsSerializer(many=True,source='offerdetails_set')
    image = serializers.ImageField(required=False, allow_null=True)
    
    class Meta:
        model=Offers
        fields = ['id','user','title','description','created_at','updated_at','details','image','min_price','min_delivery_time','user_details']

        depth=3

    def create(self, validated_data):
        user=self.context['request'].user
        details_data = validated_data.pop('offerdetails_set', [])  # Verwende den richtigen Key
        #image = self.context['request'].FILES.get('image')  # Bild aus request holen
        min_price = None
        min_delivery_time = None

        validated_data['user'] = user

        offer = Offers.objects.create(**validated_data)

        # if image:
        #     validated_data['image'] = image  # Bild speichern


        for detail_data in details_data:
            detail = OfferDetails.objects.create(offer=offer, **detail_data)
            if min_price is None or detail.price < min_price:
                min_price = detail.price
                print(detail.price)
            if min_delivery_time is None or detail.delivery_time_in_days < min_delivery_time:
                min_delivery_time = detail.delivery_time_in_days
        
        offer.min_price = min_price
        offer.min_delivery_time = min_delivery_time
        offer.save()
        return offer  # Rückgabe des erstellten Objekts
