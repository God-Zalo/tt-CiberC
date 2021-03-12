from django.shortcuts import render
from .serializers import ProductSerializer, FileSerializer
from .models import Product, FileUpload
from rest_framework import generics, status



from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import connection

# Create your views here.


class InventoryListView(generics.ListAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()

class FileUploadView(APIView):
	def post(self, request):
		serializer = FileSerializer(data = request.data)
		if serializer.is_valid(rise_exception=True):
			serializer.save()
			return  Response(serializer.data, status=status.HTTP_201_CREATED)


	def get(self, request):
		files = FileUpload.objects.all()
		serializer = FileSerializer(files, many=True)
		return Response({"files": serializer.data})