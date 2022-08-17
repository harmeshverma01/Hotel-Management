from django.urls import path
from .views import RoomDetailView, RoombookedView, RoomView, HotelView

urlpatterns = [
    path('rooms/', RoomView.as_view()),
    #path('room-avaiable/', RoomAvaiableView.as_view()),
    path('rooms-booked/', RoombookedView.as_view()),
    path('room-details', RoomDetailView.as_view()),
    path('Hotels', HotelView.as_view())
]