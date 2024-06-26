from enum import Enum

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from goalwise.models import TimeStampMixin


class Status(Enum):
    NOT_STARTED = "Not Started"
    COMPLETE = "Completed"
    IN_PROGRESS = "In Progress"


class Tag(TimeStampMixin):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Day(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Task(TimeStampMixin):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    duration = models.DurationField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    days_of_week = models.ManyToManyField(Day)

    def __str__(self):
        return self.title


class TaskStatus(TimeStampMixin):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[(s.value, s.name) for s in Status],
        default=Status.NOT_STARTED.value,
    )

    def __str__(self):
        return f"{self.task.title} - {self.date}"
