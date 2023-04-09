from django.db import models
from core.base_model import BaseModel
from user.models.base import User


class Feedback(BaseModel):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiving_user')
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title