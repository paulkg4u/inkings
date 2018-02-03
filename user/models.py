from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employee(User):
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Team(models.Model):
    teamName = models.CharField(max_length=100)

    def __unicode__(self):
        return self.teamName
