from rest_framework import serializers
from yuhutest.apps.tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "title", "description", "due_date", "user")
        extra_kwargs = {'user': {'required': False}}
        read_only_fields = ("id", )