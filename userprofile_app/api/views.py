from rest_framework import viewsets
from userprofile_app.models import Profile
from userprofile_app.api.serializers import ProfileSerializer
from .permissions import IsOwnerOrReadOnly

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    