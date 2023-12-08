# Generated by Django 4.2.7 on 2023-11-28 23:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_day_remove_task_days_of_week_task_days_of_week'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('Not Started', 'NOT_STARTED'), ('Completed', 'COMPLETE'), ('In Progress', 'IN_PROGRESS')], default='Not Started', max_length=20)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.DeleteModel(
            name='TaskCompletion',
        ),
        migrations.AddField(
            model_name='taskstatus',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
    ]
