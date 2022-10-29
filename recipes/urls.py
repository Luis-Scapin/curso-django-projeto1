from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path(r'', views.home, name="home"),  # Home
    path(r'recipes/category/<int:category_id>/', views.category, name="category"),
    path(r'recipes/<int:id>/', views.recipe, name="recipe"),  # Recipe
]
