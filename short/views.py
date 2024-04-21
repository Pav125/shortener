from django.shortcuts import render, get_object_or_404, redirect
from .forms import AnonymousShortForm
from .models import AnonymousShortify
from django.http import Http404

import hashlib
import string
import random

def generate_short_url(original_url):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    hash_object = hashlib.sha256(original_url.encode())
    hash_digest = hash_object.hexdigest()

    return hash_digest[:4]+random_string[:3]

# Create your views here.
def index(request):
    short_url = None
    if request.method == 'POST':
        form = AnonymousShortForm(request.POST)

        if form.is_valid():
            original_url = form.cleaned_data['url']
            existing_url = AnonymousShortify.objects.filter(url=original_url).first()
            if existing_url:
                short_url = existing_url.short_url
            else:
                shorturl = generate_short_url(original_url)
                short_url = request.build_absolute_uri('/')+shorturl
                # while AnonymousShortify.objects.filter(url=original_url).first()
                while AnonymousShortify.objects.filter(short_url=short_url).exists():
                    shorturl = generate_short_url(original_url)
                    short_url = request.build_absolute_uri('/')+shorturl
                url = AnonymousShortify.objects.create(url = original_url, short_url = short_url)
                url.save()
    else:
        form = AnonymousShortForm()
    context = {
        'form' : form,
        'short_url' : short_url if short_url else None
    }


    return render(request, 'short/index.html', context)

def redirect_short_url(request, slug):
    base_url = request.scheme + '://' + request.get_host()
    absolute_url = base_url + '/' + slug
    short_url = get_object_or_404(AnonymousShortify, short_url = absolute_url)
    return redirect(short_url.url)


# def custom_404_view(request, exception):
#     return render(request, 'short/404.html', status=404)
