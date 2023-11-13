from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeHome.as_view(), name='home'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path("<slug:slug>/", views.RecipeDetail.as_view(), name="single_recipe"),

]
