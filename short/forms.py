from django import forms
from .models import AnonymousShorti

class AnonymousShortForm(forms.ModelForm):
    class Meta:
        model = AnonymousShorti
        fields = ('url',)
        labels = {
            'url' : 'Enter URL here '
        }

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label = 'Email')
    message = forms.CharField(label='Message',widget=forms.Textarea())

    