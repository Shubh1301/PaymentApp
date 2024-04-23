from django.urls import path
from .models import User
from .views import UserAPIView,ApplyLoanAPIView

urlpatterns = [
    path('create-user', UserAPIView.as_view(), name='create-user'),
    path('apply-loan', ApplyLoanAPIView.as_view() ,name='apply-loan'),
]