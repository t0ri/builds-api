from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User

        
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def sign_up(request, format='json'):
    """ 
    Creates the user. 
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Code from https://github.com/ShubhamBansal1997/token-authentication-django/blob/master/myproject/myproject/views.py
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def sign_in(request):
    """
    Returns token if user exists.
    """
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'user': user.id},
                    status=status.HTTP_200_OK)