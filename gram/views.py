from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from blog.models import Gram, Report
from upload.forms import GramUpload
from .forms import ReportForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

# Create your views here.


def grams_list(request):
    '''
    Displays three columns by two rows of all individual
        :model:`blog.Gram` posted by users.

    Paginates the request result up to six posts with clickable load more
        to load a further six posts.

    **Context**:

    ``grams``
        A list of all Gram objects ordered by creation date.
    ``page_obj``
        A paginated list of Grams.

    **Template**:

    :template:`gram/grams_list.html`
    '''
    # Fetch all Gram posts
    grams = Gram.objects.all().order_by('-created_on')

    # Paginate the results
    paginator = Paginator(grams, 6)  # Show 6 grams per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gram/grams_list.html', {'page_obj': page_obj})


def gram_detail(request, pk):
    '''
    Displays a single detailed :model:`blog.Gram` view.

    **Context**:

    ``gram``
        An instance of the Gram model.

    **Template**:

    :template:`gram/gram_detail.html`
    '''
    # Retrieve the specific Gram object or return a 404 error if not found
    gram = get_object_or_404(Gram, pk=pk)
    return render(request, 'gram/gram_detail.html', {'gram': gram})


@login_required
def gram_action(request, pk):
    '''
    Like or unlike a :model:`blog.Gram` and refresh the page
        to update the count.

    Delete a stored :model:`blog.Gram` and redirect to the
        :views:`gram.gram_detail`

    Checks if the user is the owner of Gram before
        allowing the user to delete its Gram.

    **Context**:

    ``gram``
        An instance of the Gram model.

    **Template**:

    None
    '''
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
                return render(
                    request, '403.html'
                )  # Forbidden if user is not the photographer

        gram.save()  # Save changes if any like/unlike action was performed
        return redirect(
            'gram_detail', pk=pk
        )  # Redirect to the gram detail page

    return redirect(
        'gram_detail', pk=pk
    )  # Redirect to the gram detail page if not POST


@login_required
def edit_gram(request, pk):
    '''
    Checks whether the user is the owner of Gram or not. If not,
        it will redirect to :views:`gram.gram_detail` and display
            the warning message.

    Checks if the user is the owner of Gram, and it will proceed
        to :views:`gram.edit_gram` to edit Gram and
            update the stored :model:`blog.Gram`.

    **Context**:

    ``gram``
        An instance of the Gram model.
    ``form``
        An instance of the GramUpload form.

    **Template**:

    :template:`gram/edit_gram.html`
    '''
    gram = get_object_or_404(Gram, pk=pk)

    # Check if the logged-in user is the owner of the gram
    if request.user != gram.photographer:
        messages.warning(request, "You are not authorised to edit this gram.")
        return redirect('grams')  # Redirect to the grams list page

    if request.method == 'POST':
        form = GramUpload(request.POST, request.FILES, instance=gram)
        if form.is_valid():
            form.save()
            messages.success(request, "Gram updated successfully!")
            return redirect(
                'gram_detail', pk=gram.pk
            )  # Redirect to the gram detail page
    else:
        form = GramUpload(
            instance=gram
        )  # Populate the form with the current gram data

    return render(request, 'gram/edit_gram.html', {'form': form, 'gram': gram})


@login_required
def report_gram(request, pk):
    '''
    Checks if the user have already submitted the :model:`blog.Report` before
        to prevent spamming and redirect to :views:`gram.gram_detail`
            and display a warning message.

    Checks if the user have not submitted the :model:`blog.Report` yet
        and redirect to :views:`gram.gram_detail` and display the
            success message once submitted.

    **Context**:

    ``gram``
        An instance of the Gram model.
    ``form``
        An instance of the ReportForm form.

    **Template**:

    :template:`gram/report_gram.html`
    '''
    gram = get_object_or_404(Gram, id=pk)

    # Check if the user has already reported this gram
    if Report.objects.filter(gram=gram, user=request.user).exists():
        messages.warning(
            request, "You have already reported this gram."
        )  # Danger message
        return redirect('gram_detail', pk=gram.id)

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.gram = gram
            report.user = request.user
            report.save()
            messages.success(
                request, "You have successfully reported this gram."
            )  # Success message
            return redirect(
                'gram_detail', pk=gram.id
            )  # Redirect to gram detail after reporting
    else:
        form = ReportForm()

    return render(request, 'gram/report_gram.html', {'form': form})
