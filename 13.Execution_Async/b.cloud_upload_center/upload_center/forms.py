from django import forms

# Implement `UploadFileForm` form here

class UploadFileForm(forms.Form):
    file_name = forms.CharField(max_length=30, min_length=3)
    file = forms.FileField()
