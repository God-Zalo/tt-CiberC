from django.urls import path
from .views import InventoryList

urlpatterns = [
	path ('inventory/', InventoryList.as_view(), name='inventory-list'),
]