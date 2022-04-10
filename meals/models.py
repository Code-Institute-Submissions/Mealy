from django.db import models
from django.contrib.auth.models import User         
# Create your models here.

class Ingredient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, unique=True)
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-in_stock"]


class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    meal_name = models.CharField(max_length=200)
    planned = models.BooleanField(default=False)
    ingredients = models.ManyToManyField(Ingredient,blank=True)
    meal_description = models.TextField(max_length=1000, default="Yummy meal description goes here")
    
    
    def __str__(self):
        return self.meal_name

    class Meta:
        ordering = ["-planned"]
