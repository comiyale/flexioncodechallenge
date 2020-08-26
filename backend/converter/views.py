from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ConverterSerializer

from .converter import Converter

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
            
            try:
                response = converter.convert()
            except:
                response = "Invalid"
            
            return Response(response)

        else:
            return Response({"errors": serializer.errors})