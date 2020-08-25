import json
import pint

from rest_framework import serializers

ureg = pint.UnitRegistry()

class Converter:
    def __init__(self, value, initial_unit, desired_unit, student_response, isTemp=False):
        self.value = value
        self.isTemp = isTemp
        self.initial_unit = initial_unit
        self.desired_unit = desired_unit
        self.student_response = student_response

    def __convert_temp(self):
        temp_units_quantity = ureg.Quantity
        
        temp_units = {
            "kelvin": ureg.kelvin,
            "rankine": ureg.rankine,
            "celsius": ureg.celsius,
            "fahrenheit": ureg.fahrenheit
        }

        initial_value = temp_units_quantity(self.value, temp_units[self.initial_unit])
        
        desired_value = initial_value.to(self.desired_unit).magnitude
        
        return desired_value

    def __convert_units(self):
        units = {
                'cups': ureg.cup,
                'liters': ureg.liters,
                'gallons': ureg.gallons,
                'teaspoons': ureg.teaspoon,
                'cubic_inch': ureg.cubic_inch,
                'tablespoon': ureg.tablespoon,
            }

        initial_value = self.value * units[self.initial_unit]
        desired_value = initial_value.to(self.desired_unit).magnitude
        
        return desired_value

    def __check_compatibility(self):
        compatible_units = list(ureg.get_compatible_units(self.initial_unit))
        is_compatible = str(self.desired_unit) in compatible_units

        return is_compatible
    
    def __approx_to_tenth(self, value):
        return round(value, 2)

    def __compare_answer(self, desired_value):

        approx_student_response = self.__approx_to_tenth(self.student_response)
        approx_desired_value = self.__approx_to_tenth(desired_value)
        is_equal = (approx_student_response == approx_desired_value)
        return is_equal

    def convert(self):
        if self.isTemp:
            desired_value = self.__convert_temp()
            is_valid = self.__compare_answer(desired_value)

            if is_valid:
                return "correct"
            else:
                return "incorrect"
            
        elif self.isTemp==False:
            desired_value = self.__convert_units()
            is_valid = self.__compare_answer(desired_value)
        
            if is_valid:
                return "correct"
            else:
                return "incorrect"
            
        else:
            return "Invalid"