from django.urls import path,include
from rest_framework.routers import DefaultRouter
from orders_app.api.views import OrdersViewset

router = DefaultRouter()
router.register(r'orders',OrdersViewset)

urlpatterns = [
    path('',include(router.urls))
]