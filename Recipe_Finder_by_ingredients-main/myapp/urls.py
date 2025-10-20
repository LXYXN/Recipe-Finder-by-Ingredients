from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('recipes/', views.get_recipes, name='get_recipes'),
    path('recipes/<int:recipe_id>/', views.recipe_details, name='recipe_details'),
]
