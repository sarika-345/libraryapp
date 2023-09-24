from django.shortcuts import render
from book.models import Book
from book.serializers import BookSerializer,UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,AllowAny

class Userviewset(viewsets.ModelViewSet):   #non primary key
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()
    serializer_class=UserSerializer



class Bookviewset(viewsets.ModelViewSet):
    # permission_classes = [AllowAny, ]
    queryset = Book.objects.all()
    serializer_class=BookSerializer