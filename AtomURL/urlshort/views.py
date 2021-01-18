from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import ShortURL
from .forms import CreateNewShortURL
from datetime import datetime
import random, string

# Create your views here.
def home(request):
    return render(request, 'home.html')

def redirect_old(request, url):
    current_obj = ShortURL.objects.filter(short_url=url)
    if len(current_obj) == 0:
        return render(request, '404.html')
    context = {'obj':current_obj[0]}
    return render(request, 'redirect.html', context)

def createShortURL(request):
    if request.method == 'POST':
        form = CreateNewShortURL(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['long_url']
            random_chars_list = list(string.ascii_letters)
            random_chars = ''
            for i in range(6):
                random_chars += random.choice(random_chars_list)
            while len(ShortURL.objects.filter(short_url=random_chars)) != 0:
                for i in range(6):
                    random_chars += random.choice(random_chars_list)
            date = datetime.now()
            s = ShortURL(long_url=original_website, short_url=random_chars, time_date_created=date)
            s.save()

            return render(request, 'urlcreated.html', {'chars':random_chars})

    else:
        form=CreateNewShortURL()
        context={'form': form}
        return render(request, 'create.html', context)

def registerPage(request):
    return render(request, 'register.html')

def loginPage(request):
    return render(request, 'login.html')

def page_redirect(request, url):
    get_url = ShortURL.objects.filter(short_url=url)
    return redirect(get_url.first().long_url)