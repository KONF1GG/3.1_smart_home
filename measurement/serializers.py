from django.forms.fields import ImageField
from rest_framework import serializers

from .models import Sensor, Measurment


class MeasurementSerializer(serializers.ModelSerializer):
    image = ImageField(max_length=None, allow_empty_file=True)
    class Meta:
        model = Measurment
        fields = ['id', 'temperature', 'date_time', 'sensor', 'image']


class SensorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
