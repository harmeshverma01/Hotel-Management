from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RoomSerializer
from .models import room
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class Roomview(APIView):
    serializer_class = RoomSerializer

    
    def get(self, request, id=None):
        user = room.objects.all()
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)
                    
    
    def post(self, request):
        user = room.objects.create_user(
            name = request.data.get('name'),
            booking_date = request.data.get('booking_date'),
            room_number = request.data.get('room_number'),
        )
        serializer =  RoomSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    