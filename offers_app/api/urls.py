from django.urls import path,include
from rest_framework.routers import DefaultRouter
from offers_app.api.views import OffersViewset,OfferDetailsViewset

router = DefaultRouter()
router.register(r'offers',OffersViewset)
router.register(r'offerdetails',OfferDetailsViewset)

urlpatterns = [
    path('',include(router.urls)),
]
