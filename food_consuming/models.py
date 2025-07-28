from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    carbs = models.DecimalField(max_digits=6, decimal_places=2)
    proteins = models.DecimalField(max_digits=6, decimal_places=2)
    fats = models.DecimalField(max_digits=6, decimal_places=2)
    calories = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)



class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)