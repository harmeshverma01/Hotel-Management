from email.mime import image
from django.db import models

from user.models import User

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=150)
    booking_date = models.DateTimeField(null=True)
    room_number = models.IntegerField(null=True)
    image = models.ImageField()
    floor = models.IntegerField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='User', null=True)
    
    def __str__(self) -> str:
        return self.name
    