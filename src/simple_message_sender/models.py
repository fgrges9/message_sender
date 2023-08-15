from django.db import models
from django.contrib.auth.models import User, AbstractUser
from rest_framework import serializers


class Message(models.Model):
    text = models.TextField(max_length=1024, blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
# Create your models here.


class ExtendedUser(User):
    uuid = models.UUIDField(null=False, primary_key=True)
    chat_id = models.IntegerField(null=True)