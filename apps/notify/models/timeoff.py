from django.db import models
from user.models.base import User
from core.base_model import BaseModel


class Timeoff(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timeoff = models.PositiveIntegerField()
    date = models.DateField()
    reason = models.TextField()

    def __str__(self) -> str:
        return f"{self.user} takes time off for {self.timeoff} hours on {self.date}"