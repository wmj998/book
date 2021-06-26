from django.urls import path, include

from cart import views

urlpatterns = [
    path('index/', views.index),
    path('checkout/', views.checkout),
    path('add_cart/', views.add_cart),
    path('delete_cart/', views.delete_cart),
    path('delete_all/', views.delete_all),

]
