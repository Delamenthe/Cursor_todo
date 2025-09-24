from django.contrib import admin
from .models import TaskList, Task


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "emoji", "default_background_key", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "list", "is_completed", "due_date", "sort_order", "created_at")
    list_editable = ("is_completed", "sort_order")
    search_fields = ("title", "description")
    list_filter = ("is_completed", "due_date", "created_at")
