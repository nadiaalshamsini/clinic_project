from rest_framework import serializers
from .appointment import Appointment
from .patient import Patient
from .nutritionist import Nutrionist

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'app_id',
            'patient',
            'nutritionist',
            'date',
            'time',
            'status',
            'type',
            'notes',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['app_id', 'created_at', 'updated_at']
