from django.db import models
from accounts.models import User


class Benefactor(models.Model):
    EXPEREINCE_CHOICES = (
        (0, "مبتدی"),
        (1, "متوسط"),
        (2, "متخصص")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices=EXPEREINCE_CHOICES, default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)

class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return self.filter(charity__user=user)

    def related_tasks_to_benefactor(self, user):
        return self.filter(assigned_benefactor__user=user)

    def all_related_tasks_to_user(self, user):
        return self.filter(
            models.Q(assigned_benefactor__user=user) |
            models.Q(charity__user=user) |
            models.Q(state='P')
        )



class Task(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female")
    )

    STATE_CHOICES = (
        ("P", "Pending"),
        ("W", "Waiting"),
        ("A", "Assigned"),
        ("D", "Done")
    )

    assigned_benefactor = models.ForeignKey(Benefactor, on_delete=models.SET_NULL, null=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(null=True, blank=True)
    age_limit_to = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    gender_limit = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default="P")
    title = models.CharField(max_length=60)
    objects = TaskManager()



