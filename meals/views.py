from django.shortcuts import render
from django.views import generic
from .models import Meal


# Create your views here.
class MealList(generic.ListView):
    model = Meal
    queryset = Meal.objects.order_by("-planned")
    template_name = "index.html"
