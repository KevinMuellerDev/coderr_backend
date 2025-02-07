from django.urls import path, include

urlpatterns = [
    path('',include('auth_app.api.urls')),
    path('',include('userprofile_app.api.urls'))
]
