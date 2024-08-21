from django.shortcuts import render, redirect
from . import views

# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        return redirect('grams')  # Redirect to the gram page if logged in
    return render(request, "blog/index.html")  # Render the homepage if not logged in