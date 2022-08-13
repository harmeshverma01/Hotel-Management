from django.urls import path
from .views import RoomDetailView, Roomview

urlpatterns = [
    path('rooms/<int:uuid>', Roomview.as_view()),
    path('room-details/', RoomDetailView.as_view())

    
]