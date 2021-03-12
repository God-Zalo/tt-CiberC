from rest_framework import serializers
from .models import Product, FileUpload


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'


class FileSerializer(serializers.Serializer):

	id = serializers.IntegerField(read_only=True)
	filename = serializers.CharField(required=True, max_length=50)
	date = serializers.DateField(required=False)
	file = serializers.FileField(required=True)
	summary = serializers.CharField(required=False, max_length=250, allow_blank=True)

	def create(self, validated_data):
		return FileUpload.objects.create(**validated_data)

	