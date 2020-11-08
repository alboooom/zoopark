from rest_framework import serializers
from .models import Animal, Place, Сonnection, Worker, Kind


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('id', 'name', 'kind', 'place', 'image', 'updated_at', 'created_at')


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('name', 'iron_grate', 'width', 'length', 'updated_at', 'created_at')


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('name', 'age', 'growth', 'weight', 'zoo_animals', 'updated_at', 'created_at')


class KindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kind
        fields = ('name', 'danger', 'image', 'updated_at', 'created_at')


class ConectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Сonnection
        fields = ('animal', 'worker', 'date_joined')