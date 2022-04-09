from django.shortcuts import render
from django.views import generic
from .models import Meal, Ingredient
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


# Create your views here.
class MealList(LoginRequiredMixin, generic.ListView):
    model = Meal
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.pk)
        user_meals = Meal.objects.filter(user=user)
        context = {
            'user_meals': user_meals,
        }
        return render(request, self.template_name, context)
    

class ShopList(LoginRequiredMixin, generic.ListView):
    model = Meal
    template_name = "list.html"

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.pk)
        user_meals = Meal.objects.filter(user=user)
        context = {
            'user_meals': user_meals,
        }
        return render(request, self.template_name, context)
