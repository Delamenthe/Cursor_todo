from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import TaskList, Task
from .serializers import TaskListSerializer, TaskSerializer


class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all().order_by("-created_at")
    serializer_class = TaskListSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related("list").all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]

# Create your views here.
