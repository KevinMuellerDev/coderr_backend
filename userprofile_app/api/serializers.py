from rest_framework import serializers
from userprofile_app.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        