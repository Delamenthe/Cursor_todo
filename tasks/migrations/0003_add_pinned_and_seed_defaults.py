from django.db import migrations, models


def pin_defaults(apps, schema_editor):
  TaskList = apps.get_model('tasks', 'TaskList')
  TaskList.objects.filter(title__in=["Мой день", "Задачи"]).update(pinned=True)


class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0002_seed_default_lists'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(pin_defaults),
    ]


