from rest_framework import viewsets, permissions
from .models import App, Task
from .serializers import AppSerializer, TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [permissions.IsAdminUser]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['create', 'update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['post'])
    def upload_screenshot(self, request, pk=None):
        task = self.get_object()
        screenshot = request.FILES.get('screenshot')
        if screenshot:
            task.screenshot = screenshot
            task.save()
            return Response({'status': 'Screenshot uploaded'})
        return Response({'status': 'Failed to upload screenshot'}, status=400)
