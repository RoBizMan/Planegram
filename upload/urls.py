from django.urls import path
from . import views

urlpatterns = [
    path('', views.gram_post, name='gram_post'),
    path('add-plane/', views.add_plane, name='add_plane')
]