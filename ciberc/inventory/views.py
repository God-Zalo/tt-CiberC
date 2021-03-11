from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from rest_framework import generics

# Create your views here.


class InventoryList(generics.ListAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()
