from django.urls import path
from .views import InventoryList, FileUpload

urlpatterns = [
	path ('', InventoryList.as_view()),
	path ('fileupload/', FileUpload.as_view()),
]