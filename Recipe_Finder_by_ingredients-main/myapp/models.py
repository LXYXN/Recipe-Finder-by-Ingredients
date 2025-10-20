from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
    cooking_time = models.IntegerField()  # in minutes
    difficulty = models.CharField(max_length=50)
    instructions = models.TextField()
    image_url = models.URLField()

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
