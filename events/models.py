from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Events(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='events_image', null=True, blank=True)
    description_mini = RichTextField(null=True, blank=True)
    description_full = RichTextField(null=True, blank=True)
    style = RichTextField(null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    active = models.BooleanField(default=1)
