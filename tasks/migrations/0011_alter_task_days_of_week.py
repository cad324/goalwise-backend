# Generated by Django 4.2.7 on 2023-11-22 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_alter_task_days_of_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='days_of_week',
            field=models.JSONField(),
        ),
    ]
