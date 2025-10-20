import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import SearchHistory

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def get_recipes(request):
    if request.method == 'GET':
        ingredients = request.GET.get('ingredients')
        api_key = '30bac7aec89f44e794f5f59aabd28bb8'
        url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey={api_key}'
        response = requests.get(url)
        recipes = response.json()

        # Save search history
        search_history = SearchHistory(user=request.user, query=ingredients)
        search_history.save()

        return JsonResponse(recipes, safe=False)

@login_required
def recipe_details(request, recipe_id):
    api_key = '30bac7aec89f44e794f5f59aabd28bb8'
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}'
    response = requests.get(url)
    details = response.json()
    return JsonResponse(details, safe=False)
