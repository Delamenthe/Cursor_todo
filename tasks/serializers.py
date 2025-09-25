from rest_framework import serializers
from .models import TaskList, Task, BackgroundAsset


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
    custom_background = serializers.ImageField(allow_null=True, required=False)
    background_asset = serializers.PrimaryKeyRelatedField(queryset=BackgroundAsset.objects.all(), allow_null=True, required=False)
    background_asset_obj = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TaskList
        fields = [
            "id",
            "title",
            "emoji",
            "pinned",
            "default_background_key",
            "custom_background",
            "background_asset",
            "background_asset_obj",
            "created_at",
            "updated_at",
            "tasks",
        ]

    def update(self, instance: TaskList, validated_data):
        # Handle explicit clearing of custom background when null is provided
        if "custom_background" in validated_data and validated_data.get("custom_background") is None:
            # Delete file from storage without saving immediately
            if instance.custom_background:
                instance.custom_background.delete(save=False)
            instance.custom_background = None
            # Remove from validated_data so default update() doesn't try to set None again
            validated_data.pop("custom_background", None)

        return super().update(instance, validated_data)

    def get_background_asset_obj(self, obj: TaskList):
        asset = obj.background_asset
        if not asset:
            return None
        return BackgroundAssetSerializer(asset, context=self.context).data


class BackgroundAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundAsset
        fields = ["id", "name", "file", "created_at"]

