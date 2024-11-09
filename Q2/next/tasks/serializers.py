from rest_framework import serializers
from .models import App, Task

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id', 'name', 'description', 'points']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'app', 'points_earned', 'screenshot', 'completed']
