from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Unit, UnitType
from .serializers import UnitSerializer, UnitTypeSerializer, ConverterSerializer

from .logic.converter import Converter

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


class ConverterView(APIView):
    name = 'convert'

    def post(self, request):
        serializer = ConverterSerializer(data=request.data)

        if serializer.is_valid():
            valid_data = serializer.data

            value = valid_data.get("value")
            isTemp = valid_data.get("isTemp")
            initial_unit = valid_data.get("initial_unit")
            desired_unit = valid_data.get("desired_unit")
            student_response = valid_data.get("student_response")

            converter = Converter(value=value, initial_unit=initial_unit, desired_unit=desired_unit, isTemp=isTemp, student_response=student_response)
            
            try:
                response = converter.convert()
            except:
                response = "Invalid"
            
            return Response(response)

        else:
            return Response({"errors": serializer.errors})