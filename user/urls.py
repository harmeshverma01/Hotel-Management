from django.urls import path
from .views import Userview, Loginview

urlpatterns = [
    path('users/', Userview.as_view()),
    path('login/', Loginview.as_view())
    
]
