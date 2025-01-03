# book/form.py
from django import forms

class UploadedFileForm(forms.Form):
    title = forms.CharField(label="Title", max_length=255)
    description = forms.CharField(label="Description", widget=forms.Textarea, required=False)
    visibility = forms.BooleanField(label="Public Visibility", required=False)
    cost = forms.DecimalField(label="Cost", max_digits=10, decimal_places=2, required=False)
    year_published = forms.IntegerField(label="Year of Publication", required=False)
    file = forms.FileField(label="Upload File")
