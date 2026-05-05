from rest_framework import serializers
from .nutritionist import Nutrionist
from .clinic import Clinic

class NutritionistSerializer(serializers.ModelSerializer):
    clinic_name = serializers.CharField(source='clinic.name', read_only=True)
    
    class Meta:
        model = Nutrionist
        fields = [
            'nut_id', 'clinic', 'clinic_name', 'first_name', 'last_name',
            'email', 'phone', 'password', 'specialization', 'overview',
            'profile_image', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['nut_id', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
            'email': {'required': True},
            'first_name': {'required': True, 'min_length': 2},
            'last_name': {'required': True, 'min_length': 2},
        }
    
    def create(self, validated_data):
        """تشفير كلمة المرور عند الإنشاء"""
        password = validated_data.pop('password')
        nutrionist = Nutrionist(**validated_data)
        nutrionist.set_password(password)
        nutrionist.save()
        return nutrionist