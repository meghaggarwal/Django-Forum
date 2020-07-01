from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return  self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_update = models.DateTimeField(default=timezone.now)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter= models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

class Post(models.Model):
    message = models.TextField(max_length=4000)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)






