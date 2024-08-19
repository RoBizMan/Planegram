from django.urls import path
from . import views

urlpatterns = [
    path('', views.grams_list, name='grams'),  # List of all grams
    path('<int:pk>/', views.gram_detail, name='gram_detail'),  # Detail view for a specific gram
]