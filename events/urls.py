from django.urls import path

from events.views import events, event_page

app_name = 'events'

urlpatterns = [
    path('', events, name='events'),
    path('<int:event_id>/', event_page, name='event_page')
]
