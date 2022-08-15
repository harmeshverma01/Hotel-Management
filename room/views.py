from math import floor
from unicodedata import name
from rest_framework.views import APIView

from ..user.utils import admin_required
from .serializers import RoomSerializer
from room.models import Room
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class RoomView(APIView):
    serializer_class = RoomSerializer
    
    def get(self, request, id=None):
        user = Room.objects.all()
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)
                    
class RoombookedView(APIView):
    serializer_class = RoomSerializer
    
    def get(self, request, id=None):
        user = Room.objects.all()
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)
                    
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data) 
        
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
             


        
                     