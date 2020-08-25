from rest_framework import serializers

from .models import Unit, UnitType


class UnitTypeSerializer(serializers.ModelSerializer):
    
    units = serializers.SlugRelatedField(
       many=True,
       read_only=True,
       slug_field='name'
    )

    class Meta:
        model = UnitType
        fields = ['pk', 'name', 'units']

class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = ['pk', 'name', 'custom', 'unit_type']


class ConverterSerializer(serializers.Serializer):
    value = serializers.FloatField()
    isTemp = serializers.BooleanField(default=False)
    initial_unit = serializers.CharField(required=True, max_length=100)
    desired_unit = serializers.CharField(required=True, max_length=100)