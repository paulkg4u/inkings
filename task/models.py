from django.db import models
from user.models import User, Team
from project.models import Project

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField(default="")
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    isComplete = models.BooleanField(default=False)
    status = models.TextField(default="")
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.DO_NOTHING)
    team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return self.name
