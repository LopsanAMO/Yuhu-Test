from django.urls import path
from .views import create_user, LoginView

urlpatterns = [
    path('', create_user, name='create_user'),
    path('login/', LoginView.as_view(), name='login'),
]