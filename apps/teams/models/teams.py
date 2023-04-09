# Django
from django.db import models

# Project
from user.models import User
from core.base_model import BaseModel


class Project(BaseModel):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    deadline = models.DateField()

    def __str__(self):
        return self.name