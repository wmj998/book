from django.contrib import admin
from django.urls import path, include

from user import views

urlpatterns = [
    path('register/', views.register),
    path('register_success/', views.register_success),
    path('login/', views.login_user),
    path('login_success/', views.login_success),
    path('logout/', views.logout_user),
    path('index/', views.index),
    path('delete/', views.delete_user),
    path('exchange/', views.exchange),
    path('query/', views.query),
    path('exchange_query/', views.exchange_query),

]
