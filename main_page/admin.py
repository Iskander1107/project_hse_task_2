from django.contrib import admin
from main_page.models import MainMenu, ContactWithUs
# Register your models here.


@admin.register(ContactWithUs)
class ContactWithUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_numbers', 'email')
    fields = ('name', 'phone_numbers', 'email', 'create_time')


@admin.register(MainMenu)
class MainMenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'sort', 'active')
    fields = ('title', 'link', 'sort', 'active')
