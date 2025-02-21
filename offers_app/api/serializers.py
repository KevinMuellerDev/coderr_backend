from rest_framework import serializers
from offers_app.models import OfferDetails,Offers
from django.contrib.auth.models import User
from userprofile_app.models import Profile
from django.db.models import Min

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
    details = OfferDetailsLinkedSerializer(many=True,source='offerdetails')

    
    class Meta:
        model=Offers
        fields = ['id','user','title','description','created_at','updated_at','details','image','min_price','min_delivery_time','user_details']
        extra_kwargs={
            'image':{'required':False}
        }



class OfferInputSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True) 
    user_details = UserDetailsSerializer(source='user',read_only=True)
    details = OfferDetailsSerializer(many=True,source='offerdetails')
    image = serializers.ImageField(required=False, allow_null=True)
    
    class Meta:
        model=Offers
        fields = ['id','user','title','description','created_at','updated_at','details','image','min_price','min_delivery_time','user_details']
        depth=3

    def new_min_price(self, instance):
        min_price = instance.offerdetails.aggregate(Min('price'))['price__min']
        new_min_price=0.0
        if min_price != None:
            new_min_price = min_price
        return new_min_price
    
    def new_min_delivery_time(self,instance):
        min_delivery_time = instance.offerdetails.aggregate(Min('delivery_time_in_days'))['delivery_time_in_days__min']
        new_min_delivery_time = 7
        if min_delivery_time != None:
            new_min_delivery_time = min_delivery_time
        return new_min_delivery_time

    def create(self, validated_data):
        user=self.context['request'].user
        min_price = None
        min_delivery_time = None

        validated_data['user'] = user
        details_data = validated_data.pop('offerdetails', [])

        is_business_user = Profile.objects.get(user=user)
        print(is_business_user)

        if is_business_user.type == 'customer':
            raise serializers.ValidationError(
                {'error': 'User ist not a Business User'})

        offer = Offers.objects.create(**validated_data)

        for detail_data in details_data:
            detail = OfferDetails.objects.create(offer=offer, **detail_data)
            if min_price is None or detail.price < min_price:
                min_price = detail.price
            if min_delivery_time is None or detail.delivery_time_in_days < min_delivery_time:
                min_delivery_time = detail.delivery_time_in_days
        
        offer.min_price = min_price
        offer.min_delivery_time = min_delivery_time
        offer.save()
        return offer  
    
    def update(self, instance, validated_data):
        details_data = validated_data.pop('offerdetails', [])
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        
        for detail_data in details_data:
            offer_type = detail_data.get('offer_type')

            OfferDetails.objects.update_or_create(
                offer=instance, 
                offer_type=offer_type,
                defaults=detail_data
            )

        instance.min_price = self.new_min_price(instance=instance)
        instance.min_delivery_time = self.new_min_delivery_time(instance=instance)
        instance.save()

        return instance
    

