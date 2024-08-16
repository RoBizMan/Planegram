from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import GramUpload
from blog.models import Aircraft

# View for handling Gram uploads
def upload_gram(request):
    if request.method == 'POST':
        form = GramUpload(request.POST, request.FILES)
        if form.is_valid():
            gram = form.save(commit=False)
            gram.photographer = request.user
            gram.save()
            return redirect('home')
    else:
        form = GramUpload()
    
    return render(request, 'upload/upload.html', {'form': form})

# View for adding a new plane
@csrf_exempt
def add_plane(request):
    if request.method == 'POST':
        plane_make = request.POST.get('planeMake')
        plane_model = request.POST.get('planeModel')

        if plane_make and plane_model:
            new_plane = Aircraft.objects.create(
                plane_make=plane_make,
                plane_model=plane_model,
            )

            return JsonResponse({
                'success': True,
                'newPlane': {
                    'id': new_plane.id,
                    'make': new_plane.plane_make,
                    'model': new_plane.plane_model
                }
            })
        else:
            return JsonResponse({'success': False, 'error': 'Missing fields'}, status=400)

    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)
