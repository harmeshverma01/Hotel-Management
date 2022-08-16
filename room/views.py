from .serializers import HotelSerializer, RoomSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from user.utils import admin_required
from room.models import Room, Hotel
from rest_framework import status

# Create your views here.

class RoomView(APIView):
    serializer_class = RoomSerializer
    permission_classes = [admin_required]
    
    def get(self, request, id=None):
        user = Room.objects.all()
        price = request.GET.get('price', None)
        if price is not None:
            user = user.filter(price=price)
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)
                    
                    
class RoombookedView(APIView):
    serializer_class = RoomSerializer
    permission_classes = [admin_required]
    
    def get(self, request, id=None):
        user = Room.objects.all()
        date = request.GET.get('date', None)
        if date is not None:
            user = user.filter(date=date)
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
        except:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, id=None):
       user = Room.objects.get(id=id)
       user.delete()
       return Response(({"message": "Room is deleted"}),status=status.HTTP_204_NO_CONTENT)                


class HotelView(APIView):
    serializer_class = HotelSerializer
    permission_classes = [admin_required]
    
    def get(self, request, id=None):
        hotel = Hotel.objects.all()
        address = request.GET.get('address', None)
        if address is not None:
            hotel = hotel.filter(address=address)
        serializer = self.serializer_class(hotel, many=True)
        return Response(serializer.data)
   
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
       
    def patch(self, request, id=None):
        try:
            hotel = Hotel.objects.get()
            serializer  = self.serializer_class(hotel, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)   
        
    def delete(self, request, id=None):
        hotel = Hotel.objects.get()
        hotel.delete()
        return Response({'message': 'hotel is deleted'}, status=status.HTTP_204_NO_CONTENT)     
