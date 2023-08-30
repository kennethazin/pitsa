from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('payment/', views.payment, name='payment'),
    path('confirmation/', views.confirmation, name='confirmation')
]
