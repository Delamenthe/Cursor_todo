from django.db import migrations


def create_default_lists(apps, schema_editor):
    TaskList = apps.get_model('tasks', 'TaskList')
    defaults = [
        {"title": "Задачи", "emoji": "📝", "default_background_key": "midnight"},
        {"title": "Мой день", "emoji": "🌞", "default_background_key": "sunset"},
    ]
    for data in defaults:
        TaskList.objects.get_or_create(title=data["title"], defaults=data)


def remove_default_lists(apps, schema_editor):
    TaskList = apps.get_model('tasks', 'TaskList')
    TaskList.objects.filter(title__in=["Задачи", "Мой день"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_lists, remove_default_lists),
    ]


