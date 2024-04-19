from django.urls import path
from .models import User
from .views import UserAPIView

urlpatterns = [
    path('create-user', UserAPIView.as_view(), name='create-user'),
    
]