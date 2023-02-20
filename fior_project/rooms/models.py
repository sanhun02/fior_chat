from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    users = {}

class Msg(models.Model):
    room = models.ForeignKey(Room, related_name='msgs', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='msgs', on_delete=models.CASCADE)
    content = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('data_added',)