from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from yuhutest.apps.tasks.models import Task


class TaskModelViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()

    @extend_schema(
        description="Get list of tasks",
        operation_id="Tasks.List",
        tags=["Tasks"],
    )
    def list(self, request, *args, **kwargs):
        return super(TaskModelViewSet, self).list(request, *args, **kwargs)

    @extend_schema(
        description="Crete a Task",
        operation_id="Task.Create",
        tags=["Tasks"],
    )
    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return super(TaskModelViewSet, self).create(request, *args, **kwargs)

    @extend_schema(
        description="Get a Task",
        operation_id="Task.Retrieve",
        tags=["Tasks"],
    )
    def retrieve(self, request, *args, **kwargs):
        return super(TaskModelViewSet, self).retrieve(request, *args, **kwargs)

    @extend_schema(
        description="Delete a Task",
        operation_id="Task.Delete",
        tags=["Tasks"],
    )
    def destroy(self, request, *args, **kwargs):
        return super(TaskModelViewSet, self).destroy(request, *args, **kwargs)

    @extend_schema(
        description="Update a Task",
        operation_id="Task.Put",
        tags=["Tasks"],
    )
    def update(self, request, *args, **kwargs):
        return super(TaskModelViewSet, self).update(request, *args, **kwargs)

    @extend_schema(
        description="Partial Update Task",
        operation_id="Task.Patch",
        tags=["Tasks"],
    )
    def partial_update(self, request, *args, **kwargs):
        return super(TaskModelViewSet, self).partial_update(request, *args, **kwargs)
