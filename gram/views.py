from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from blog.models import Gram
from upload.forms import GramUpload
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def grams_list(request):
    # Fetch all Gram posts
    grams = Gram.objects.all().order_by('-created_on')
    
    # Paginate the results
    paginator = Paginator(grams, 10)  # Show 10 grams per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gram/grams_list.html', {'page_obj': page_obj})

def gram_detail(request, pk):
    # Retrieve the specific Gram object or return a 404 error if not found
    gram = get_object_or_404(Gram, pk=pk)
    return render(request, 'gram/gram_detail.html', {'gram': gram})
    
@login_required
def gram_action(request, pk):
    # This view handles like/unlike and delete actions
    gram = get_object_or_404(Gram, pk=pk)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'like':
            gram.love.add(request.user)
        elif action == 'unlike':
            gram.love.remove(request.user)
        elif action == 'delete':
            if request.user == gram.photographer:
                gram.delete()  # Delete the gram
                return redirect('grams')  # Redirect to the grams list page
            else:
                return render(request, '403.html')  # Forbidden if user is not the photographer
        
        gram.save()  # Save changes if any like/unlike action was performed
        return redirect('gram_detail', pk=pk)  # Redirect to the gram detail page
    
    return redirect('gram_detail', pk=pk)  # Redirect to the gram detail page if not POST

@login_required
def edit_gram(request, pk):
    gram = get_object_or_404(Gram, pk=pk)

    # Check if the logged-in user is the owner of the gram
    if request.user != gram.photographer:
        messages.error(request, "You are not authorised to edit this gram.")
        return redirect('grams')  # Redirect to the grams list page

    if request.method == 'POST':
        form = GramUpload(request.POST, request.FILES, instance=gram)
        if form.is_valid():
            form.save()
            messages.success(request, "Gram updated successfully!")
            return redirect('gram_detail', pk=gram.pk)  # Redirect to the gram detail page
    else:
        form = GramUpload(instance=gram)  # Populate the form with the current gram data

    return render(request, 'gram/edit_gram.html', {'form': form, 'gram': gram})
