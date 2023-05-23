from rest_framework.serializers import ModelSerializer
from .models import Student , Places

class Stserializer(ModelSerializer) :
    class Meta :
        model = Student
        fields = '__all__'

class Plserializer(ModelSerializer) :
    class Meta :
        model = Places
        fields = '__all__'