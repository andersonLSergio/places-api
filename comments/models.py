from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{ self.user.username }'s comment"