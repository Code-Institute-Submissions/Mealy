from .models import Meal, Ingredient
from django import forms




class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        widgets = {'ingredients': forms.widgets.CheckboxSelectMultiple() }
        fields = ("meal_name", "meal_description", "planned", "ingredients",)

