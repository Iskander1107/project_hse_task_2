from django.db import models

# Create your models here.


class Events(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='events_image', null=True)
    description_mini = models.TextField(null=True)
    description_full = models.TextField(null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    active = models.BooleanField(default=1)
