from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    opening_time = models.TextField()
    min_age_allowed = models.IntegerField()

    def __str__(self):
        return self.name