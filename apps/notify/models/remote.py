from django.db import models
from core.base_model import BaseModel
from user.models.base import User


class Remote(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField()