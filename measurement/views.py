from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, ListCreateAPIView, CreateAPIView

from .models import Measurment, Sensor
from .serializers import SensorDetailSerializer, MeasurementSerializer


class API(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class APIputch(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class APIMesurments(CreateAPIView):
    get_queryset = Measurment.objects.all()
    serializer_class = MeasurementSerializer

