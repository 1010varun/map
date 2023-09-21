from django.urls import path
from .views import *

urlpatterns = [
    path('helprequest', help.as_view(), name = 'helpRequest'),
    path('getNotifications', getNotifications.as_view(), name = 'notifications'),
]