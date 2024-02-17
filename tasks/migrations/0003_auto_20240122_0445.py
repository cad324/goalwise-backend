# Generated by Django 4.2.7 on 2024-01-22 04:45

from django.db import migrations

def add_days(apps, schema_editor):
    Day = apps.get_model('tasks', 'Day')
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for day_name in days:
        Day.objects.create(name=day_name)


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_tag_id_alter_task_id_alter_taskstatus_id'),
    ]

    operations = [
        migrations.RunPython(add_days),
    ]
