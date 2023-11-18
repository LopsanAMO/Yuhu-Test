from django.urls import path, include
from rest_framework.routers import DefaultRouter
from yuhutest.apps.tasks.api.v1.views import TaskModelViewSet


task_router = DefaultRouter()
task_router.register(r'task', TaskModelViewSet, basename='tasks')


urlpatterns = [
    path('', include(task_router.urls)),
]
