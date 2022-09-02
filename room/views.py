
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
        room = Room.objects.all()
        start_price = request.GET.get('start_price', None)
        end_price = request.GET.get('end_price', None)
        if start_price is not None or end_price is not None:
            room = room.filter(price__range = [start_price, end_price ])
        serializer = self.serializer_class(room, many=True)
        return Response(serializer.data)
                    
                    
class RoombookedView(APIView):
    serializer_class = RoomSerializer
    permission_classes = [admin_required]
    
    def get(self, request, id=None):
        room = Room.objects.all()
        booking_date = request.GET.get('booking_date', None)
        checkout_date = request.GET.get('checkout_date', None)
        if booking_date is not None or checkout_date is not None:
            room = room.filter(date__range = [booking_date, checkout_date])
        serializer = self.serializer_class(room , many=True)
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


# class RaturantView(APIView):
#     serializer_class = HotelSerializer
    
#     def get(self, request, id=None):
#         Resturant = Hotel.objects.all()
#         serializer = self.serializer_class(Resturant, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         resturant = Hotel.objects.create(
#             name = request.get('name'),
#             floor = request.get('floor'),
#             room = request.get('room'),
#             rating = request.get('rating'),
#             rewiew = request.get('rewiew'),
#             address = request.get('address'),
#         )
#         resturant.save()
#         serializer = self.serializer_class()
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
    
#     def patch(self, request, id=None):
#         try:
#             resturant = Hotel.objects.get(id=id)
#             serializer = self.serializer_class(resturant, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
#         except:
#             return Response(serializer.errors, status=status.H)
        
#     def delete(self, request, id=None):
#         returant = Hotel.objects.get(id=id)
#         returant.delete()
#         return Response({'message':'Resturant is not avaible'}, status=status.HTTP_404_NOT_FOUND)