from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskStatusViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'tasks/(?P<ids>\d+(?:,\d+)*)/status', TaskStatusViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
