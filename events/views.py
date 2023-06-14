from django.shortcuts import render
from main_page.models import MainMenu
# Create your views here.

def events(request):
    content = {
        'menu': MainMenu.objects.all()
    }
    return render(request, 'events.html', content)