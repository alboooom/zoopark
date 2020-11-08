from rest_framework import viewsets, pagination
from .models import Animal, Place, Worker, Kind, Сonnection
from .serializers import AnimalSerializer, PlaceSerializer, \
    WorkerSerializer, KindSerializer, ConectionSerializer

from .filters import KPfilter


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all().order_by('id')
    filter_class = KPfilter
    filter_fields = ('name',)
    serializer_class = AnimalSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return AnimalSerializer
        if self.action == 'retrieve':
            return AnimalSerializer
        return AnimalSerializer


class PlacelViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()


class WorkerViewSet(viewsets.ModelViewSet):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


class KindViewSet(viewsets.ModelViewSet):
    serializer_class = KindSerializer
    queryset = Kind.objects.all()


class ConnectionViewSet(viewsets.ModelViewSet):
    serializer_class = ConectionSerializer
    queryset = Сonnection.objects.all()
