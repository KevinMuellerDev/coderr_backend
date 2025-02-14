from rest_framework import serializers
from userprofile_app.models import Profile
from django.contrib.auth.models import User
from datetime import datetime

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['pk','username', 'first_name', 'last_name']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['uploaded_at']

    def update(self, instance, validated_data):
        file = validated_data['file']
        if instance.file != file:
            instance.uploaded_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return super().update(instance, validated_data)
    

class CustomerProfileSerializer(serializers.ModelSerializer):
    user = CustomUserDetailsSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['user','file','uploaded_at','type']


class BusinessProfileSerializer(serializers.ModelSerializer):
    user = CustomUserDetailsSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['user','file','location','tel','description','working_hours','type']