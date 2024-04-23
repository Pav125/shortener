from django.shortcuts import render, get_object_or_404, redirect
from .forms import AnonymousShortForm, ContactForm
from .models import AnonymousShorti
from django.core.mail import send_mail
from django.contrib import messages

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

    urls = AnonymousShorti.objects.order_by('-created_at')[:7]

    short_url = None
    form = AnonymousShortForm()
    
    if request.method == 'POST':
        form = AnonymousShortForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['url']
            existing_url = AnonymousShorti.objects.filter(url=original_url).first()
            if existing_url:
                short_url = existing_url.short_url
            else:
                shorturl = generate_short_url(original_url)
                short_url = request.build_absolute_uri('/')+shorturl
                while AnonymousShorti.objects.filter(short_url=short_url).exists():
                    shorturl = generate_short_url(original_url)
                    short_url = request.build_absolute_uri('/')+shorturl
                url = AnonymousShorti.objects.create(url=original_url, short_url=short_url)
                url.save()  

    # Determine which template to render based on user authentication
    template = 'short/index.html'

    context = {
        'form': form,
        'short_url': short_url,
        'urls' : urls
    }
    
    return render(request, template, context)



def redirect_short_url(request, slug):
    base_url = request.scheme + '://' + request.get_host()
    absolute_url = base_url + '/' + slug
    short_url = get_object_or_404(AnonymousShorti, short_url = absolute_url)
    return redirect(short_url.url)


def page_not_found(request, exception):
    return render(request, 'short/404.html', status=404)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['message']
            subject = 'Contact Form'
            message = f'Name: {name}\nEmail: {email}\n\n Message: {text}'

            send_mail(
                subject,
                message,
                'devipavan825@gmail.com',
                ['devipavan824@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Your message was sent successfully.')
            return redirect('index')
        else:
            form = ContactForm()

    return render(request, 'short/contact.html')