from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')  # Makes it read-only

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'city', 'date', 'created_by', 'image', 'event_category']
