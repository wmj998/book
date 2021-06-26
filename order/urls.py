from django.urls import path
from order import views

urlpatterns = [
    path('index/', views.index),
    path('state/', views.state),
]
