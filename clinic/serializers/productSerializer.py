from rest_framework import serializers
from models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'product_id',
            'nutritionist',
            'name',
            'price',
            'quantity',
            'img',
            'type',
            'description',
            'is_available',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['product_id', 'created_at', 'updated_at']
