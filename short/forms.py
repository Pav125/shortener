from django import forms
from .models import AnonymousShortify

class AnonymousShortForm(forms.ModelForm):
    class Meta:
        model = AnonymousShortify
        fields = ('url',)
