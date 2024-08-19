from django.urls import path
from . import views

urlpatterns = [
    path('', views.grams_list, name='grams'),
]