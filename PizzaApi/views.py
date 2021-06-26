from rest_framework import serializers
from rest_framework.views import APIView
from PizzaApi.models import Pizza, PizzaSize, PizzaTopping, PizzaType
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PizzaSerializer

# from django.http import JsonResponse
# from rest_framework.parsers import JSONParser

# Create your views here.

@api_view(['GET'])
def PizzaList(request):
    pizzas = Pizza.objects.all()
    serializer = PizzaSerializer(pizzas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def PizzaList_Size(request, size_id):
    pizzas = Pizza.objects.filter(size_id = size_id)
    serializer = PizzaSerializer(pizzas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def PizzaList_Type(request, type_id):
    pizzas = Pizza.objects.filter(type_id = type_id)
    serializer = PizzaSerializer(pizzas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CreatePizza(request):
    pass        


@api_view(['POST'])
def UpdatePizza(request,pizza_id):
    pass

@api_view(['DELETE'])
def DeletePizza(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    pizza.delete()
    return Response({'Message':'Success'})
