from rest_framework import serializers
from models.patientInitialInfo import PatientInitialInfo
from .patient import Patient
class PatientInitialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInitialInfo
        fields = '__all__'
