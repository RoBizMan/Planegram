from django.urls import path
from . import views

urlpatterns = [
    # List of all grams
    path('', views.grams_list, name='grams'),
    # Detail view for a specific gram
    path('<int:pk>/', views.gram_detail, name='gram_detail'),
    # View for handling actions
    path('<int:pk>/action/', views.gram_action, name='gram_action'),
    # Edit a specific gram
    path('<int:pk>/edit/', views.edit_gram, name='edit_gram'),
    # Report incorrect details
    path('<int:pk>/report/', views.report_gram, name='report_gram'),
]
