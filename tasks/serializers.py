from rest_framework import serializers
from .models import TaskList, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "list",
            "title",
            "description",
            "is_completed",
            "due_date",
            "sort_order",
            "created_at",
            "updated_at",
        ]


class TaskListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = TaskList
        fields = [
            "id",
            "title",
            "emoji",
            "default_background_key",
            "custom_background",
            "created_at",
            "updated_at",
            "tasks",
        ]

