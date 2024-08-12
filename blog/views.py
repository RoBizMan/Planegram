from django.shortcuts import render
from django.views import generic
from .models import Gram

# Create your views here.

def homepage(request):
    return render(
        request, "blog/index.html"
    )