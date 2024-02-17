from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer, TaskStatusSerializer
import logging

logger = logging.getLogger(__name__)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request):
        task_data = request.data
        task_data["user"] = request.user.id
        serializer = TaskSerializer(data=task_data)

        if request.user.id != task_data["user"]:
            logger.error(f"[TaskViewSet] User ID mismatch. Request User ID: {request.user.id}, Task User ID: {task_data.get('user')}")
            return Response({"message": "You do not have permission to update this task."}, status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            serializer.save()
            logger.info(f"[TaskViewSet] Task created\nData: {request.data}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        logger.error(f"[TaskViewSet] Could not create task\Response: {request.data}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            task = self.get_object()
        except Task.DoesNotExist:
            return Response({"message": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        if task.user != request.user:
            return Response({"message": "You do not have permission to update this task."}, status=status.HTTP_403_FORBIDDEN)

        serializer = TaskSerializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        task_data = request.data
        task_data["user"] = request.user.id
        serializer = TaskSerializer(data=task_data)
        
        try:
            task = self.get_object()
        except Task.DoesNotExist:
            return Response({"message": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        if task.user != request.user:
            return Response({"message": "You do not have permission to update this task."}, status=status.HTTP_403_FORBIDDEN)

        serializer = TaskSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            task = self.get_object()
        except Task.DoesNotExist:
            logger.error(f"[TaskViewSet] Task not found\nUser: {request.user.id}")
            return Response({"message": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        if task.user == request.user:
            task.delete()
            logger.info(f"[TaskViewSet] Task deleted\nUser: {request.user.id}")
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.error(logger.info(f"[TaskViewSet] Task could not be deleted\nUser: {request.user.id}"))
            return Response({"message": "You do not have permission to delete this task."}, status=status.HTTP_403_FORBIDDEN)
        
class DayViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        pass
    
    def destroy(self, request, *args, **kwargs):
        pass
    
    def update(self, request, *args, **kwargs):
        pass
    
    def partial_update(self, request, *args, **kwargs):
        pass
    
class TaskStatusViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskStatusSerializer

    def list(self, request, ids=None, *args, **kwargs):
        id_list = [int(id_) for id_ in ids.split(',')] if ids else []
        tasks = Task.objects.filter(id__in=id_list)
        serializer = self.serializer_class(tasks, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        pass