from django.shortcuts import render
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