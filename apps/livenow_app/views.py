from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def eat(request):
    return render(request, 'eat_now.html')

def lift(request):
    return render(request, 'lift_now.html')