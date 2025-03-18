from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet,CustomerProfileViewSet,BusinessProfileViewSet
router = DefaultRouter()
router.register(r'profile',ProfileViewSet)
router.register(r'profiles/customer',CustomerProfileViewSet,basename='customer-profile')
router.register(r'profiles/business',BusinessProfileViewSet,basename='business-profile')
urlpatterns = [
    path('',include(router.urls))
]
