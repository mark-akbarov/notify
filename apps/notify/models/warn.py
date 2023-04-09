from django.db import models
from user.models.base import User
from core.base_model import BaseModel


class Warn(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    warning = models.TextField()

    def __str__(self) -> str:
        return f"{self.user} - {self.warning}"