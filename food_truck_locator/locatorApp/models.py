from django.db import models

# Create your models here.
class FoodTruckInfo(models.Model):
    locationId = models.IntegerField(default=0)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    foodItems = models.CharField(max_length=300)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.name} at {self.address}"

