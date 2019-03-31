from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    rate = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{ self.user.username }'s review'"