from django.db import models
import datetime

# Create your models here.
class ClientAllManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class ClientAllDeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=True)

class Client (models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    all_clients = ClientAllManager()
    all_deleted_clients = ClientAllDeletedManager()

    def __str__(self):
        return self.name
    
    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = datetime.datetime.now()
        self.save()

    def un_delete(self):
        self.is_deleted = False
        self.save()

    class Meta:
        ordering = ["-timestamp", ]


class Contact (models.Model):
    contact = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="contacts")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    title = models.CharField(max_length=255)
    office_number = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client.name + ' ' + self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ["-timestamp", ]