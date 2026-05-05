from rest_framework import serializers
from models.workshop import Workshop

class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = [
            'workshop_id',
            'nutritionist',
            'title',
            'date',
            'time',
            'place',
            'type',
            'overview',
            'img',
            'link',
            'status',
            'num_participants',
            'max_participants',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['workshop_id', 'created_at', 'updated_at']
