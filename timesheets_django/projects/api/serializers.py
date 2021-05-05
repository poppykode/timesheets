from rest_framework import serializers
from projects.models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('client','name','start_date','end_date','notes')

class TaskSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ('project','resource','task_name','start_date','end_date','notes','projects')