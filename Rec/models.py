from django.db import models
# Create your models here.

from django.conf import settings
from django.utils import timezone


class Stud(models.Model):
    user = models.CharField(max_length=50)

    def __str__(self):
        return self.user


class Question(models.Model):

    SUB = (
    ('Python','Python'),
    ('JQUERY', 'jQuery'),
    ('JavaScript','JavaScript'),
)
    question = models.CharField(max_length=200)
    subj = models.CharField(max_length=10, choices=SUB, default='Python')
    answer = models.TextField(max_length=200, null = True, blank = True)
    easy = models.BooleanField(default=True)
    medium = models.BooleanField(default=True)
    hard = models.BooleanField(default=True)

    def __str__(self):
        return self.question