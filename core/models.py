from django.db import models
from features.models import Feature
from comments.models import Comment
from reviews.models import Review
from location.models import Location

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    features = models.ManyToManyField(Feature)
    comments = models.ManyToManyField(Comment)
    reviews = models.ManyToManyField(Review)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name