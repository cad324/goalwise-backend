# Generated by Django 4.2.3 on 2023-10-19 02:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accountability_score', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('task_count', models.PositiveIntegerField(default=0)),
                ('consistency', models.FloatField(default=0.5)),
                ('account_age', models.PositiveIntegerField(default=0)),
                ('screen_time', models.PositiveIntegerField(default=0)),
                ('task_retention', models.FloatField(default=0.95)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Metrics',
                'verbose_name_plural': 'User Metrics',
            },
        ),
    ]
