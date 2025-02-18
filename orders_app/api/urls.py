from django.urls import path,include
from rest_framework.routers import DefaultRouter
from orders_app.api.views import OrdersViewset,OrderCount,OrderCompletedCount

router = DefaultRouter()
router.register(r'orders',OrdersViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('order-count/<int:business_user_id>/',OrderCount.as_view(),name='order_count'),
    path('completed-order-count/<int:business_user_id>/',OrderCompletedCount.as_view(),name='completed_order_count')
]