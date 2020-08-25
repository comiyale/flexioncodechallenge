from django.shortcuts import render

from rest_framework import generics

from .models import Unit, UnitType
from .serializers import UnitSerializer, UnitTypeSerializer

#CRUD FOR VIEWS

class CreateListUnit(generics.ListCreateAPIView):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()
    name = 'unit-list'


class DetailUnit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    name = 'unit-detail'


class CreateListUnitType(generics.ListCreateAPIView):
    serializer_class = UnitTypeSerializer
    queryset = UnitType.objects.all()
    name = 'unittype-list'


class DetailUnitType(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer
    name = 'unittype-detail'