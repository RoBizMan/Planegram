from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from blog.models import Gram

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

    if request.method == 'POST':
        if 'like' in request.POST:
            gram.love.add(request.user)
        elif 'unlike' in request.POST:
            gram.love.remove(request.user)
        gram.save()
        return redirect('gram_detail', pk=pk)

    return render(request, 'gram/gram_detail.html', {'gram': gram})