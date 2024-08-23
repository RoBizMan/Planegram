from django import forms
from blog.models import Gram
import datetime
from django.forms.widgets import ClearableFileInput

# Custom ClearableFileInput to override the default behavior


class CustomClearableFileInput(ClearableFileInput):
    template_name = 'widgets/custom_clearable_file_input.html'

    # Override to remove the "Currently" section
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['is_initial'] = False  # Hides the "Currently" field
        return context


class GramUpload(forms.ModelForm):
    class Meta:
        model = Gram
        fields = ["date_photographed", "caption", "image", "plane"]
        widgets = {
            "date_photographed": forms.DateInput(
                attrs={"type": "date", "max": str(datetime.date.today())}
                ),
            "image": CustomClearableFileInput(),  # Displays the "Choose a
            # File" field only
        }
