from turtle import title
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    date_posted = models.DateTimeField(default =timezone.now)


