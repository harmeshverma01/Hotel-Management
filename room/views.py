from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User
from .serializers import RoomSerializer
from room.models import Room
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class Roomview(APIView):
    serializer_class = RoomSerializer
    

    
    def get(self, request, id=None):
        user = Room.objects.all()
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)
                    
    
    def post(self, request):
        user = Room.objects.create_user(
            name = request.data.get('name'),
            booking_date = request.data.get('booking_date'),
            room_number = request.data.get('room_number'),
        )
        serializer =  RoomSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


class RoomDetailView(APIView):
    serializer_class = RoomSerializer
     
     
    def get(self, request, id=None):
        room = Room.objects.filter(user__id=id)
        serializer = self.serializer_class(room, many=True)
        return Response(serializer.data)
    
    def patch(self, request, id=None):
        try:
            user = Room.objects.get(id=id)
            serializer = self.serializer_class(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Room.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
    def delete(self, request, id=None):
       user = Room.objects.get(id=id)
       user.delete()
       return Response(({"message": "Room is deleted"}),status=status.HTTP_204_NO_CONTENT)                
             