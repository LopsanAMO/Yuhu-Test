from django.urls import path, include
from yuhutest.apps.users.views import UserView

urlpatterns = [
    path('api/users/', include('yuhutest.apps.users.api.v1.urls')),
    path('users/', UserView.as_view(), name='users'),
]