from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import GramUpload
from blog.models import Aircraft


@login_required
def upload_gram(request):
    '''
    Handles the uploading of a new Gram post by the authenticated user.

    If the request method is POST, it processes the form submission. If the form is 
        valid, it saves :model:`blog.Gram` instance with the current user as the 
            photographer and redirects to :views:`gram.grams_list`.
    
    If the request method is GET, it initialises an empty GramUpload form.

    **Context**:

    ``form``
        An instance of the GramUpload form for uploading a new Gram.

    **Template**:

    :template:`upload/upload.html`
    '''
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
