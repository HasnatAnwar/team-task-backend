from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny , IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

@api_view(["POST"])
# @permission_classes([AllowAny])
def register(request):

    # the serializer will auto validate teh data as we add the validate_data paramenter in serializer
    
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors,status=400)

@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):

    # these two fields are required
    username = request.data.get("username")
    password = request.data.get("password")

    # authentication process this will authenticate the user 
    # this is django build in function
    
    user = authenticate(username=username,password=password)

    if user:
        login(request,user)
        return Response({"message":"Logged in"})

    return Response({"error":"Invalid credentials"},status=400)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({"message":"Logged out"})


# to get the csrf token it is for development

@api_view(["GET"])
def csrf(request):
    return Response({"csrfToken": get_token(request)})


# to get the current stat either logged in or logged out
# extra layer to the session handling in frontend

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    return Response({'id': request.user.id, 'username': request.user.username, 'email': request.user.email})
