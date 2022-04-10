from .models import Meal
from django import forms




class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ("meal_name", "meal_description", "planned", "ingredients")

