from django.db.models import fields
from rest_framework import serializers
from .models import *

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('name', 'size','type' ,'toppings')
        depth = 1
    

    

    