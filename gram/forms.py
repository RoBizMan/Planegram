# forms.py
from django import forms
from blog.models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['message']