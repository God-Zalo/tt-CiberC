from django.contrib import admin
from .models import Product, FileUpload
from pyxlsb import open_workbook

# Register your models here.

admin.site.register(Product)

# Define admin class
class FileAdmin(admin.ModelAdmin):
	def summary(self, obj):

		my_json = {}
		elements = 0
		total_price = 0
		average_price = 0

		try:
			with open_workbook(obj.file.url) as wb:
				with wb.get_sheet(1) as sheet:
					for row in sheet.rows():
						for col in row:

							# Total elements ignoring first row as header
							if (col.c == 1 and col.r >= 1):
								elements = elements + col.v
								
							# Average price ignoring first row as header
							if (col.c == 2 and col.r >= 1):
								total_price = total_price + col.v


			average_price = total_price/elements

			my_json["elements"] = elements
			my_json["average_price"] = average_price

		except:
			print("Could not read File")
		return my_json

	list_display = ['filename', 'summary']

#Register Admin class with associated model
admin.site.register(FileUpload, FileAdmin)
