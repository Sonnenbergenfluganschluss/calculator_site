from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Calculation
from .forms import CalculatorForm
import math

def home(request):
    if request.user.is_authenticated:
        form = CalculatorForm()
        history = Calculation.objects.filter(user=request.user).order_by('-created_at')[:10]
        return render(request, 'calculator/home.html', {'form': form, 'history': history})
    else:
        return render(request, 'calculator/home.html')

@login_required
def calculate(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            expression = form.cleaned_data['expression']
            try:
                result = eval(expression)  # Осторожно! В продакшне используйте безопасные парсеры (например, `tinyexpr`)
                Calculation.objects.create(
                    user=request.user,
                    expression=expression,
                    result=result
                )
                return render(request, 'calculator/result.html', {'result': result})
            except:
                return render(request, 'calculator/error.html', {'error': 'Неверное выражение'})
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'calculator/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'calculator/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')