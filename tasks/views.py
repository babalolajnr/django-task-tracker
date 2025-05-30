from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from tasks.serializers import TaskSerializer
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all() # pyright:ignore
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user) # pyright:ignore

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
