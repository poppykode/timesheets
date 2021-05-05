import datetime
from django.db import models
from django.db.models.deletion import CASCADE
from clients.models import Client
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class ProjecstAllManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class ProjectsAllDeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=True)


class Project (models.Model):
    client = models.ForeignKey(Client,on_delete=CASCADE,  related_name="clients")
    name = models.CharField(max_length=255)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    notes = models.TextField()
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name +' '+ self.client.name

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = datetime.datetime.now()
        self.save()

    def un_delete(self):
        self.is_deleted = False
        self.save()

    all_projects = ProjecstAllManager()
    all_deleted_projects = ProjectsAllDeletedManager()

class TaskAllManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class Task (models.Model):
    project = models.ForeignKey(Project,on_delete=CASCADE, related_name="projects")
    resource = models.ForeignKey(User,on_delete=CASCADE, related_name="resources")
    task_name = models.CharField(max_length=255)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    notes = models.TextField()
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name +' '+ self.project.name
    
    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = datetime.datetime.now()
        self.save()

    def un_delete(self):
        self.is_deleted = False
        self.save()

    all_tasks = TaskAllManager()
