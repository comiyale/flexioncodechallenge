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