from email.mime import image
from django.db import models

# Create your models here.

class room(models.Model):
    name = models.CharField(max_length=150)
    booking_date = models.DateTimeField()
    room_number = models.IntegerField()
    image = models.ImageField()
    floor = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    