from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from userprofile_app.models import Profile
from userprofile_app.api.serializers import ProfileSerializer,CustomerProfileSerializer,BusinessProfileSerializer
from .permissions import IsOwnerOrReadOnly

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def handle_exception(self, exc):
        response = super().handle_exception(exc)

        if response.status_code==405:
            return Response(
                {"detail":"Es ist nicht erlaubt das Profil eines anderen Users zu verändern."},
                status=status.HTTP_403_FORBIDDEN
            )
        return response

class CustomerProfileViewSet(viewsets.ModelViewSet):
    queryset=Profile.objects.filter(type='customer')
    serializer_class=CustomerProfileSerializer

class BusinessProfileViewSet(viewsets.ModelViewSet):
    queryset=Profile.objects.filter(type='business')
    serializer_class=BusinessProfileSerializer
    