from . import views
from django.urls import path

urlpatterns = [
    path("", views.MealList.as_view(), name="home"),
    path("list", views.ShopList.as_view(), name="shopping_list"),
    path("toggle_planned/<meal_id>", views.toggle_planned, name="toggle"),]