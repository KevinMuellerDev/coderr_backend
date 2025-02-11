from rest_framework import serializers
from offers_app.models import OfferDetails,Offers,OfferFeature
from django.contrib.auth.models import User

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['first_name','last_name','username']


class OfferFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model=OfferFeature
        fields=['feature']


class OfferDetailsSerializer(serializers.ModelSerializer):
    feature = serializers.SerializerMethodField()

    class Meta:
        model=OfferDetails
        fields=['id','title','revisions','delivery_time_in_days','price','feature','offer_type']

    def get_feature(self,obj):
        return list(obj.offerfeature_set.values_list('feature', flat=True))
    

class OfferDetailsLinkedSerializer(OfferDetailsSerializer,serializers.HyperlinkedModelSerializer):
     class Meta:
         model=OfferDetails
         fields=['id','url']



class OfferSerializer(serializers.ModelSerializer):
    user_details = UserDetailsSerializer(source='user',read_only=True)
    details = OfferDetailsLinkedSerializer(many=True,read_only=True,source='offerdetails_set')

    class Meta:
        model=Offers
        fields = ['id','user','title','image','description','created_at','updated_at','details','min_price','min_delivery_time','user_details']