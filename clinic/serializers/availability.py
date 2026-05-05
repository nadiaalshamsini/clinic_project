from rest_framework import serializers
from .availability import Availability
from .nutritionist import Nutritionist
from clinic.models import Clinic

class AvailabilitySerializer(serializers.ModelSerializer):
    clinic_name = serializers.CharField(source='clinic.name', read_only=True)
    nutrionist_name = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Availability
        fields = [
            'availability_id', 'clinic', 'clinic_name', 'nutrionist',
            'nutrionist_name', 'day', 'is_open', 'start_time', 'end_time',
            'online_start_time', 'online_end_time', 'created_at', 'updated_at'
        ]
        read_only_fields = ['availability_id', 'created_at', 'updated_at']
        extra_kwargs = {
            'clinic': {'required': True},
            'nutrionist': {'required': True},
            'day': {'required': True},
            'start_time': {'required': True},
            'end_time': {'required': True},
        }
    
    def get_nutrionist_name(self, obj):
        return f"{obj.nutrionist.first_name} {obj.nutrionist.last_name}"