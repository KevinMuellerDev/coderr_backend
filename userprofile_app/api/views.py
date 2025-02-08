from rest_framework import viewsets
from userprofile_app.models import Profile
from .serializers import ProfileSerializer
from .permissions import IsAuthenticated, IsOwner

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated,IsOwner]

    def get_queryset(self):
        """
        Sorgt dafür, dass jeder User nur sein eigenes Profil sehen kann.
        """
        return Profile.objects.filter(user=self.request.user)