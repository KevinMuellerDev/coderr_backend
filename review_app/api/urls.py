from django.urls import path,include
from rest_framework.routers import DefaultRouter
from review_app.api.views import ReviewViewset

router = DefaultRouter()
router.register(r'reviews',ReviewViewset)

urlpatterns = [
    path('',include(router.urls))
]