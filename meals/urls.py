from . import views
from django.urls import path

urlpatterns = [
    path("", views.MealList.as_view(), name="home"),
    path("list", views.ShopList.as_view(), name="shopping_list")]