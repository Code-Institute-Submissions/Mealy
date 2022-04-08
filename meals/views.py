from django.shortcuts import render
from django.views import generic
from .models import Meal, Ingredient


# Create your views here.
class MealList(generic.ListView):
    model = Meal
    queryset = Meal.objects.order_by("-planned")
    template_name = "index.html"


class ingredient_list(generic.ListView):
    model = Ingredient
    queryset = Ingredient.objects.order_by("in_stock")
    template_name = "list.html"