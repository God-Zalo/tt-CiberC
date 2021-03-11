from django.db import models

# Create your models here.

class Product(models.Model):
	serial_number = models.PositiveIntegerField()
	quantity = models.PositiveIntegerField()
	price = models.BigIntegerField()

	def __str__(self):
		return str(self.serial_number)


class FileUpload(models.Model):
	filename = models.PositiveIntegerField()
	date = models.DateField(auto_now_add=True)
	file = models.FileField(upload_to='tmp/')

	def __str__(self):
		return self.filename
