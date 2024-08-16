from django import forms
from blog.models import Gram
import datetime

class GramUpload(forms.ModelForm):
    class Meta:
        model = Gram
        fields = ["date_photographed", "caption", "image", "plane"]
        widgets = {"date_photographed": forms.DateInput(attrs={"type": "date", "max": str(datetime.date.today())})}