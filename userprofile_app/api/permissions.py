from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from django.contrib.auth.models import User

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class IsOwner(BasePermission):
    """
    Erlaubt Zugriff nur für den Besitzer des Profils.
    """

    def has_object_permission(self, request, view, obj):
        # Prüft, ob der angemeldete Benutzer der Besitzer des Profils ist
        return obj.user == request.user