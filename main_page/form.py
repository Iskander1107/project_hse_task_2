from django import forms
from django.forms import ModelForm
from main_page.models import ContactWithUs
import datetime


class ContactWithUsForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput)
    phone_numbers = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.TextInput)
    create_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'value': datetime.datetime.now(),
    }))

    class Meta:
        model = ContactWithUs
        fields = ('name', 'phone_numbers', 'email', 'create_time')
