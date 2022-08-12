from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
 # Create your views here.

class Userview(APIView):
    authentication_classes = [authentication.TokenAuthentication]
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
    
    
    
    def patch(self, request, id=None):
        try:
            user = User.objects.get(id=id)
            serializer = self.serializer_class(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    def delete(self, request, id=None):
       user = User.objects.get(id=id)
       user.delete()
       return Response(({"message": "User is deleted"}),status=status.HTTP_204_NO_CONTENT) 
    
    
class Loginview(APIView):
    serializer_class = UserSerializer
    def post(self, request):
        user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({'token': str(token[0])})
        return Response({'details': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
     