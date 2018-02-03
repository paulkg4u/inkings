from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default="")

    def __unicode__(self):
        return self.name
