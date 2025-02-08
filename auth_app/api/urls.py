from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistrationView

router = DefaultRouter()

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration')
]


