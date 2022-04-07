from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    in_stock = models.BooleanField(default=False)


class Meal(models.Model):
    meal_name = models.CharField(max_length=200, unique=True)
    planned = models.BooleanField(default=False)
    ingredients = models.ManyToManyField(Ingredient,blank=True)

