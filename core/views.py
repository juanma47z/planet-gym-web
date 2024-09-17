from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

