from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255, null=False)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name}";

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField();

    def __str__(self):
        return f"{self.title}";



