from django.shortcuts import render
from main_page.models import MainMenu
from events.models import Events

# Create your views here.


def events(request):
    content = {
        'menu': MainMenu.objects.all(),
        'events': Events.objects.all(),
    }
    return render(request, 'events.html', content)


def event_page(request, event_id):
    event = Events.objects.filter(id=event_id).first()
    content = {
        'menu': MainMenu.objects.all(),
        'event': Events.objects.filter(id=event_id).first(),
    }
    return render(request, 'event_page.html', content)