from django import forms
from .models import Shortify

class ShortForm(forms.ModelForm):
    class Meta:
        model = Shortify
        fields = ('url',)
