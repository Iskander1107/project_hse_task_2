from django.contrib import admin
# Register your models here.
from events.models import Events

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start', 'end', 'active')