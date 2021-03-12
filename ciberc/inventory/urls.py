from django.urls import path
from .views import InventoryListView, FileUploadView

urlpatterns = [
	path ('', InventoryListView.as_view()),
	path ('fileupload/', FileUploadView.as_view()),
]