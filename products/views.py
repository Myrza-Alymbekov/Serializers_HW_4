import json

from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Item, Brand, Category
from.serializers import ItemSerializer, BrandSerializer, CategorySerializer


@api_view(['POST', 'GET'])
def create_category(request):
    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(instance=categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_category(request, pk):
    category = generics.get_object_or_404(Category, pk=pk)
    if request.method == "GET":
        serializer = CategorySerializer(instance=category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
def create_brand(request):
    if request.method == "POST":
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        brands = Brand.objects.all()
        serializer = BrandSerializer(instance=brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_brand(request, pk):
    brand = generics.get_object_or_404(Brand, pk=pk)
    if request.method == "GET":
        serializer = BrandSerializer(instance=brand)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        serializer = BrandSerializer(instance=brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
def create_item(request):
    if request.method == "POST":
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(instance=items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_item(request, pk):
    item = generics.get_object_or_404(Item, pk=pk)
    if request.method == "GET":
        serializer = ItemSerializer(instance=item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        serializer = ItemSerializer(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





