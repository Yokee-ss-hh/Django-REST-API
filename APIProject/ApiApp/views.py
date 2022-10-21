from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DrinksSerializer
from .models import DrinksModel


@api_view(['GET'])
def drinks_list(request):

    drinks = DrinksModel.objects.all()
    serializer = DrinksSerializer(drinks,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def drink_in_detail(request, pk):

    drink = DrinksModel.objects.get(id=pk)
    serializer = DrinksSerializer(drink,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_new_drink(request):

    serializer = DrinksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("New item added successfully")


@api_view(['POST'])
def update_drink(request,pk):

    drink = DrinksModel.objects.get(id=pk)
    serializer = DrinksSerializer(instance=drink, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Item updated successfully")


@api_view(['DELETE'])
def delete_drink(request,pk):

    drink = DrinksModel.objects.get(id=pk)
    drink.delete()
    return Response("Item deleted successfully")



