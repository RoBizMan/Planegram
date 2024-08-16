from django.shortcuts import render
from . import views

# Create your views here.

def homepage(request):
    return render(
        request, "blog/index.html"
    )