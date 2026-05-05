from rest_framework import serializers
from models.package import Package

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            'package_id',
            'nutritionist',
            'name',
            'details',
            'price',
            'num',
            'first_payment_percentage',
            'category',
            'require_consultation',
            'status',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['package_id', 'created_at', 'updated_at']
