from django.urls import path

from manager import views

urlpatterns = [
    path('index/', views.index),
    path('book_manager/', views.book_manager),
    path('add_book/', views.add_book),
    path('update_book/', views.update_book),
    path('delete_book/', views.delete_book),
    path('order/', views.order),
    path('state/', views.state),

]
