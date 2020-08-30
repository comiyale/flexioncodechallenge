from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse

from .serializers import ConverterSerializer

from .convert import Converter, get_units


@api_view(['GET'])
def list_units(request):
        response = get_units()
        return JsonResponse(response, safe=False)

class ConverterView(APIView):
    name = 'convert'
    
    def post(self, request):
        serializer = ConverterSerializer(data=request.data)

        if serializer.is_valid():
            valid_data = serializer.data

            value = valid_data.get("value")
            initial_unit = valid_data.get("initial_unit")
            desired_unit = valid_data.get("desired_unit")
            student_response = valid_data.get("student_response")

            converter = Converter(value=value, initial_unit=initial_unit, desired_unit=desired_unit, student_response=student_response)
            
            response = converter.convert()
            
            return Response(response, status=status.HTTP_200_OK)

        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)