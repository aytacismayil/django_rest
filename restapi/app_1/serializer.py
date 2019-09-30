from .models import *
from rest_framework import serializers

class CAtegorySe(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = REST
        fields = '__all__'
