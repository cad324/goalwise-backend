from django.contrib import admin
from .models import Tag, Task, Day, TaskStatus

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    list_filter = ['user']
    search_fields = ['title', 'user__username', 'tags__name']

@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ['task', 'date']
    list_filter = ['date']

@admin.register(Day)
class Day(admin.ModelAdmin):
    list_display = ['id', 'name']