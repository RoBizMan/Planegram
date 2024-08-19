from django.urls import path
from . import views

urlpatterns = [
    path('', views.grams_list, name='grams'),  # List of all grams
    path('<int:pk>/', views.gram_detail, name='gram_detail'),  # Detail view for a specific gram
    path('<int:pk>/action/', views.gram_action, name='gram_action'),  # View for handling actions
    path('<int:pk>/edit/', views.edit_gram, name='edit_gram'), # Edit a specific gram
    path('<int:pk>/report/', views.report_gram, name='report_gram'), # Report incorrect details
]