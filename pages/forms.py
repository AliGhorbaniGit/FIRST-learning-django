from django import forms
from .models import PageDetail


class NewAutoModel(forms.ModelForm):
    class Meta :
        model = PageDetail
        fields = ['title', 'text']
