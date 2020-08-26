import json
import pint

from rest_framework import serializers

ureg = pint.UnitRegistry()

class Converter:
    temp_units = {
            "kelvin": ureg.kelvin,
            "rankine": ureg.rankine,
            "celsius": ureg.celsius,
            "fahrenheit": ureg.fahrenheit
        }

    units = {
                'cups': ureg.cup,
                'liters': ureg.liters,
                'gallons': ureg.gallons,
                'teaspoons': ureg.teaspoon,
                'cubic_inch': ureg.cubic_inch,
                'tablespoon': ureg.tablespoon,
            }
    
    def __init__(self, value, initial_unit, desired_unit, student_response):
        self.value = value
        self.initial_unit = initial_unit
        self.desired_unit = desired_unit
        self.student_response = student_response

    def convert_temp(self):
        temp_units_quantity = ureg.Quantity

        initial_value = temp_units_quantity(self.value, self.temp_units[self.initial_unit])
        
        desired_value = initial_value.to(self.desired_unit).magnitude
        
        return desired_value

    def convert_volume(self):
        initial_value = self.value * self.units[self.initial_unit]
        desired_value = initial_value.to(self.desired_unit).magnitude
        
        return desired_value

    def approx_to_tenth(self, value):
        return round(value, 1)

    def compare_answer(self, desired_value):
        approx_student_response = self.approx_to_tenth(self.student_response)
        approx_desired_value = self.approx_to_tenth(desired_value)
        is_equal = (approx_student_response == approx_desired_value)
        return is_equal
    
    def is_unit_temp(self):
        isTemp = self.initial_unit in self.temp_units.keys()
        return isTemp

    def convert(self):
        if self.is_unit_temp():
            desired_value = self.convert_temp()
            is_valid = self.compare_answer(desired_value)

            if is_valid:
                return "correct"
            else:
                return "incorrect"
            
        elif not self.is_unit_temp():
            desired_value = self.convert_volume()
            is_valid = self.compare_answer(desired_value)
        
            if is_valid:
                return "correct"
            else:
                return "incorrect"
            
        else:
            return "Invalid"