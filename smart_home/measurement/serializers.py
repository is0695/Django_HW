from rest_framework import serializers
from .models import Sensor
from .models import Measurement

# TODO: опишите необходимые сериализаторы

# class SensorSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     description = serializers.CharField()


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'date_a_time']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']