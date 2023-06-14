from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from main_page.form import ContactWithUsForm
from main_page.models import MainMenu


def index(request):
    content = {
     'menu': MainMenu()
    }
    return render(request, "index.html", content)


def contacts(request):
    content = {
        'menu': sorted(MainMenu().objects.all(), key=lambda x: x.sort)
    }
    return render(request, 'contacts.html', content)


def contact_with_us(request):
    if request.method == 'POST':
        form = ContactWithUsForm(data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        form = ContactWithUsForm()
    content = {
        'form': form,
        'menu': sorted(MainMenu().objects.all(), key=lambda x: x.sort)
    }
    return render(request, 'contact_with_us.html', content)


def olympic_hse(request):
    content = {
        'menu': sorted(MainMenu().objects.all(), key=lambda x: x.sort)
    }
    return render(request, 'olympic_hse.html', content)


def redirect_page(request):
    return redirect('/')