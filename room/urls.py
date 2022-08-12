from django.urls import path
from .views import Roomview

urlpatterns = [
    path('rooms/', Roomview.as_view())
]