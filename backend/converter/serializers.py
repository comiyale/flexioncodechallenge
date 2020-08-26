from rest_framework import serializers


class ConverterSerializer(serializers.Serializer):
    value = serializers.FloatField(required=True)
    isTemp = serializers.BooleanField(default=False)
    initial_unit = serializers.CharField(required=True, max_length=100)
    desired_unit = serializers.CharField(required=True, max_length=100)
    student_response = serializers.FloatField(required=True)