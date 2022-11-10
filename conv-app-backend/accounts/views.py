from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
