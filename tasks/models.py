from django.db import models


class TaskList(models.Model):
    title = models.CharField(max_length=200)
    emoji = models.CharField(max_length=8, blank=True, default="")
    # Either a default background key (like a gradient name) or a custom image
    default_background_key = models.CharField(max_length=64, blank=True, default="")
    custom_background = models.ImageField(upload_to="list_backgrounds/", blank=True, null=True)
    pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Task(models.Model):
    list = models.ForeignKey(TaskList, related_name="tasks", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    is_completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)
    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "-created_at"]

    def __str__(self) -> str:
        return self.title


class BackgroundAsset(models.Model):
    name = models.CharField(max_length=200, blank=True, default="")
    file = models.ImageField(upload_to="background_assets/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name or self.file.name

# Optional relation from TaskList to a reusable background asset
TaskList.add_to_class('background_asset', models.ForeignKey(BackgroundAsset, blank=True, null=True, on_delete=models.SET_NULL))
