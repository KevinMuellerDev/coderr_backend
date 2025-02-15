from rest_framework import serializers
from userprofile_app.models import Profile
from django.contrib.auth.models import User
from datetime import datetime

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields=['pk','username', 'first_name', 'last_name','file']

    def get_file(self,obj):
        profile = getattr(obj, "profile", None)
        print(profile.file)
        if profile and profile.file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(profile.file.url)
            return profile.file.url
        return None


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['uploaded_at']

    def update(self, instance, validated_data):
        
        #TODO: aktualisieren der propertys first und last name beim user

        if validated_data.get('file'):
            file = validated_data['file']
            instance.user.file=file
            print(instance.user)
            if instance.file != file:
                instance.uploaded_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        instance.user.first_name = validated_data['first_name']
        instance.user.last_name = validated_data['last_name']
        instance.user.save()
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