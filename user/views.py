from .serializers import LoginSerializer, UserSerializer
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .utils import admin_required
from .models import User

 # Create your views here.

class Userview(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated, admin_required]
    serializer_class = UserSerializer

    def get(self, request, id=None):
        user = User.objects.get(id=id)
        serializer = self.serializer_class(user)
        return Response(serializer.data)
    
    def patch(self, request, id=None):
        try:
            user = User.objects.get(id=id)
            serializer = self.serializer_class(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id=None):
       user = User.objects.get(id=id)
       user.delete()
       return Response(({"message": "User is deleted"}),status=status.HTTP_204_NO_CONTENT) 
    
    
class Loginview(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({'token': str(token[0])})
        return Response({'details': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
     
     
class UserDetailsView(APIView):
    serializer_class = UserSerializer
   
    def get(self, request, id=None):
            user = User.objects.all()
            serializer = self.serializer_class(user, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        user = User.objects.create_user(
            name = request.data.get('name'),
            email = request.data.get('email'),
            password = request.data.get('password'),
        )
        serializer =  UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def delete(self, request, id=None):
       user = User.objects.get(id=id)
       user.delete()
       return Response(({"message": "User is deleted"}),status=status.HTTP_204_NO_CONTENT) 
   