from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Chat(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField('User')
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)