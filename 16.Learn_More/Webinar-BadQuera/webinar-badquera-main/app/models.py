from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def _60_days_from_now():
    return timezone.now() + timedelta(days=60)


class College(models.Model):
    price = models.IntegerField(default=60_000)
    is_open = models.BooleanField(default=True)
    open_at = models.DateTimeField(default=timezone.now)
    close_at = models.DateTimeField(default=_60_days_from_now)
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=True)
    is_free = models.BooleanField(default=False)


class Lesson(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=None, blank=True, null=True)
    text = models.TextField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=200_000)
    colleges = models.ManyToManyField(College)
