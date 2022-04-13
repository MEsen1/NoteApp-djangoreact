from django.shortcuts import render
from .models import Notes
from .serializers import NotesSerializer
from rest_framework import viewsets
# Create your views here.

class NotesViewSet(viewsets.ModelViewSet):
    serializer_class = NotesSerializer
    queryset = Notes.objects.all();
    
    
    


