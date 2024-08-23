from django.shortcuts import render, redirect
from . import views

# Create your views here.


def homepage(request):
    if request.user.is_authenticated:
        # Redirect to the gram page if logged in
        return redirect('grams')
    # Render the homepage if not logged in
    return render(request, "blog/index.html")
