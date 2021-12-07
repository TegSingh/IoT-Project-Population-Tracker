from .models import Sensor_data
from rest_framework import serializers

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor_data
        fields = '__all__'