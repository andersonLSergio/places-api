from django.db import models

# Create your models here.
class Location(models.Model):
    line_1 = models.CharField(max_length=150)
    line_2 = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=70)
    latitude = models.DecimalField(null=True, blank=True, max_digits=15 , decimal_places=6)
    longitude = models.DecimalField(null=True, blank=True, max_digits=15 , decimal_places=6)

    def __str__(self):
        return self.line_1