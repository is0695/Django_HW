from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Sensor
from .models import Measurement
from .serializers import SensorSerializer, MeasurementSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
# TODO: опишите необходимые обработчики, рекомендуется
#  использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

# @api_view(['GET', 'POST'])
# def demo(request):
#     if request.method == 'GET':
#         sensors = Sensor.objects.all()
#         ser = SensorSerializer(sensors, many=True)
#         return Response(ser.data)
#     if request.method == 'POST':
#         return Response('ok')

# class CreateAPIView(APIView):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         ser = SensorSerializer(sensors, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         return Response('ok')

class SCreateViewSet(ModelViewSet):
    """Добавить измерение."""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SListAPIView(ListAPIView):
    """Получить список датчиков."""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        return Response('ok')

class SensorView(RetrieveAPIView):
    """Получить информацию по конкретному датчику"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MListAPIView(ListAPIView):
    """Получить все измерения"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class MCreateViewSet(ModelViewSet):
    """Добавить измерение."""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
