from django.db import models
# Create your models here.

from django.conf import settings
from django.utils import timezone


class Stud(models.Model):
    user = models.CharField(max_length=50)

    def __str__(self):
        return self.user


class Question(models.Model):
    Que = models.CharField(max_length=200)
    Ans = models.TextField(max_length=200, null = True, blank = True)
    simple = models.BooleanField(default=True)
    hard = models.BooleanField(default=True)
    very_hard = models.BooleanField(default=True)

    def __str__(self):
        return self.Que