from django.urls import path
from .views import RoomDetailView, RoombookedView, RoomView

urlpatterns = [
    path('rooms', RoomView.as_view()),
    path('rooms-booked', RoombookedView.as_view()),
    path('room-details', RoomDetailView.as_view())

    
]