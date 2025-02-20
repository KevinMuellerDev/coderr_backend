from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from orders_app.models import Orders
from userprofile_app.models import Profile 


class IsBusinessOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        business_user_id = view.kwargs.get("business_user_id")
        if not Profile.objects.filter(user_id=business_user_id,type='business').exists():
            raise PermissionDenied({"error": "Business user not found."})
        if request.user.is_authenticated and request.user.id == business_user_id:
            return True
        raise PermissionDenied({"detail": "You do not have permission to access this resource."})

class IsOwnerOrder(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.business_user)
        return obj.business_user==request.user