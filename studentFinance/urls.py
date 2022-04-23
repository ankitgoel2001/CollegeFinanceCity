from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.get_index),
    path('home/bank/', views.display_bank)
]