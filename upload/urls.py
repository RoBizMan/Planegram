from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_gram, name='upload'),
    path('add-plane/', views.add_plane, name='add_plane')
]