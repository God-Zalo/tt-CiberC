from django.shortcuts import render
from .serializers import ProductSerializer, FileSerializer
from .models import Product
from .models import FileUpload as FileUploadModel
from rest_framework import generics, status
from pyxlsb import open_workbook


from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import connection

# Create your views here.

def loader():
	serial_number = 0
	quantity = 0
	price = 0

	try:
		with open_workbook('tmp/testfile.xlsb') as wb:
				with wb.get_sheet(1) as sheet:
					for row in sheet.rows():
						for col in row:

							if (col.c == 0):
								serial_number = col.v
							
							if (col.c == 1):
								quantity = col.v

							if (col.c == 2):
								price = col.v

						print(str(serial_number) + ' ' + str(quantity) + ' ' + str(price))
						try:	
							with connection.cursor() as cursor:
								cursor.execute("INSERT INTO inventory_product (serial_number, quantity, price) VALUES (%s, %s, %s)", [serial_number, quantity, price])
								cursor.fetchall()
						except:
							pass
	except:
		print("Could not load File")


class InventoryList(generics.ListAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()

class FileUpload(APIView):
	def post(self, request):
		serializer = FileSerializer(data = request.data)
		if serializer.is_valid():
			print('is valid')
			serializer.save()
			return  Response(serializer.data, status=status.HTTP_201_CREATED)
		return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request):
		files = FileUploadModel.objects.all()
		serializer = FileSerializer(files, many=True)
		return Response({"files": serializer.data})