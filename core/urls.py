from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('registro', views.registro, name='registro')
]