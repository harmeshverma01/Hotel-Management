from enum import auto
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
    bad_count = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now=False, null=True)
    price = models.FloatField(null=True)
    
    def __str__(self) -> str:
        return self.name
    

class Hotel(models.Model):
    name = models.CharField(max_length=150)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE, related_name='Room', null=True)
    floor = models.IntegerField()
    rating = models.DecimalField(max_digits=5, decimal_places=0)
    review = models.CharField(max_length=200)
    address = models.CharField(max_length=250, null=True)