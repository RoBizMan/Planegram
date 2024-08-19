from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import GramUpload
from blog.models import Aircraft

@login_required
def upload_gram(request):
    if request.method == 'POST':
        form = GramUpload(request.POST, request.FILES)
        if form.is_valid():
            gram = form.save(commit=False)
            gram.photographer = request.user
            gram.save()
            return redirect('grams')
    else:
        form = GramUpload()
    
    return render(request, 'upload/upload.html', {'form': form})