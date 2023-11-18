from django.urls import path, include
from yuhutest.apps.tasks.views import TaskView

urlpatterns = [
    path('api/tasks/', include('yuhutest.apps.tasks.api.v1.urls')),
    path('tasks/', TaskView.as_view(), name='tasks'),
]