from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('atendente/', views.atendente, name='atendente'),
    path('garcom/', views.garcom, name='garcom'),
    path('gerente/', views.gerente, name='gerente'),
    path('relatorios/', views.relatorios, name='relatorios'),
]