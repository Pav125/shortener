from django.shortcuts import render
from .forms import ShortForm
from .models import Shortify

import hashlib

def generate_short_url(original_url):
    hash_object = hashlib.sha256(original_url.encode())
    hash_digest = hash_object.hexdigest()

    return hash_digest[:6]

# Create your views here.
def index(request):
    short_url = None
    if request.method == 'POST':
        form = ShortForm(request.POST)

        if form.is_valid():
            original_url = form.cleaned_data['url']
            shorturl = generate_short_url(original_url)
            short_url = request.build_absolute_uri('/')+shorturl
    else:
        form = ShortForm()
    context = {
        'form' : form,
        'short_url' : short_url
    }


    return render(request, 'short/index.html', context)
