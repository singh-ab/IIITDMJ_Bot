from django.shortcuts import render
from rest_framework.response import Response
from .serializers import Stserializer , Plserializer
from .models import Student , Places
from rest_framework.decorators import api_view,permission_classes
# Create your views here.
@api_view(['GET'])
def all(req) :
        s=Student.objects.all()
        b=Stserializer(s,many=True)
        return Response(b.data)
    
@api_view(['GET'])
def all2(req) :
        s=Places.objects.all()
        b=Plserializer(s,many=True)
        return Response(b.data)