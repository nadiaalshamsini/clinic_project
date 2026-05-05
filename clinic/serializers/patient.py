from rest_framework import serializers
from models.patient import Patient
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'id', 'user', 'email', 'phone', 'gender', 'birth_date',
            'address', 'height', 'start_weight', 'profile_image',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
