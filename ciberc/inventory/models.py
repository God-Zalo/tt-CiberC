from django.db import models
from pyxlsb import open_workbook
from django.conf import settings

# Create your models here.

class Product(models.Model):
	serial_number = models.PositiveIntegerField()
	quantity = models.PositiveIntegerField()
	price = models.BigIntegerField()

	def __str__(self):
		return str(self.serial_number)


class FileUpload(models.Model):
	filename = models.CharField(max_length=50)
	date = models.DateField(auto_now_add=True)
	file = models.FileField()

	def __str__(self):
		return self.filename


	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		serial_number = 0
		quantity = 0
		price = 0
		rw = 0

		with open_workbook(self.file.url) as wb:
			with wb.get_sheet(1) as sheet:
				for row in sheet.rows():
					if rw:
						for col in row:

							if (col.c == 0):
								serial_number = col.v
							elif (col.c == 1):
								quantity = col.v
							elif (col.c == 2):
								price = col.v
						
						Product.objects.create(serial_number=serial_number, quantity=quantity, price=price)
					rw+=1
