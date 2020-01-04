from rest_framework import serializers
from .models import Customer, UserDetail

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer 
        fields = ('pk','first_name', 'last_name', 'email', 'phone','address','description')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail 
        fields = ('username','first_name', 'last_name', 'email', 'password')


