from django.db import models

# Create your models here.


class MainMenu(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128)
    link = models.CharField(max_length=128)
    sort = models.PositiveIntegerField()
    active = models.BooleanField(default=1)


class ContactWithUs(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    phone_numbers = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    create_time = models.DateTimeField()

    def __str__(self):
        return f"Id: {self.id}, Имя: {self.name}, Телефон: {self.phone_numbers}, Почта: {self.email}, " \
               f"Время: {self.create_time}"