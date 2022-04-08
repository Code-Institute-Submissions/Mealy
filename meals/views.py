from django.shortcuts import render
from django.views import generic
from .models import Meal, Ingredient


# Create your views here.
class MealList(generic.ListView):
    model = Meal
    queryset = Meal.objects.order_by("-planned")
    template_name = "index.html"


class ShopList(generic.ListView):
    model = Meal
    queryset = Meal.objects.all()
    template_name = "list.html"