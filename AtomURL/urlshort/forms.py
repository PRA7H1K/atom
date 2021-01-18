from .models import ShortURL
from django import forms

class CreateNewShortURL(forms.ModelForm):
    class Meta:
        model=ShortURL

        fields = {'long_url'}

        widgets = {
            'long_url': forms.URLInput(attrs={'class': 'form-control'})
        }