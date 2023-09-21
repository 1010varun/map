from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('preRegister', preRegister.as_view(), name='preRegister'),
    path('edit', edit_Details.as_view(), name='editDetails'),
    path('getDetails', getDetails.as_view(), name='getDetails'),
    path('getLocation', getAgenciesLocation.as_view(), name='getLocationDetails'),
]
