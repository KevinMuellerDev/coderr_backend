from rest_framework.permissions import BasePermission,SAFE_METHODS
from userprofile_app.models import Profile

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        is_business_user = Profile.objects.filter(user=request.user)
        if request.method is 'POST' and is_business_user.type=='business':
            return True

        return False
        #return obj.user==request.user
    
