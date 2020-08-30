import json
import pint

from rest_framework import serializers

ureg = pint.UnitRegistry()

units = [
    {
        "temperature": ["kelvin", "rankine", "celsius", "fahrenheit"]
    },
    {
        "volume": ['cup', 'liters','gallons','teaspoons','cubic_inch', 'tablespoon']
    }
]


def get_units():
    return units

class Converter:
    temp_units = {
            "kelvin": ureg.kelvin,
            "rankine": ureg.rankine,
            "celsius": ureg.celsius,
            "fahrenheit": ureg.fahrenheit
        }

    vol_units = {
                'cup': ureg.cup,
                'liters': ureg.liters,
                'gallons': ureg.gallons,
                'teaspoons': ureg.teaspoon,
                'cubic_inch': ureg.cubic_inch,
                'tablespoon': ureg.tablespoon
            }
    
    def __init__(self, value, initial_unit, desired_unit, student_response):
        self.value = value
        self.initial_unit = initial_unit
        self.desired_unit = desired_unit
        self.student_response = student_response

    def __str__(self):
        return self.convert()
    
    def __repr__(self):
        return self.convert()

    def convert_temperature(self):
        temp_units_quantity = ureg.Quantity

        initial_value = temp_units_quantity(self.value, self.temp_units[self.initial_unit])
        desired_value = initial_value.to(self.desired_unit).magnitude
        
        return desired_value

    def convert_volume(self):
        initial_value = self.value * self.vol_units[self.initial_unit]
        desired_value = initial_value.to(self.desired_unit).magnitude
        return desired_value

    def approx_to_tenth(self, value):
        return round(value, 1)

    def compare_answer(self, desired_value):
        approx_student_response = self.approx_to_tenth(self.student_response)
        approx_desired_value = self.approx_to_tenth(desired_value)
        is_equal = (approx_student_response == approx_desired_value)

        # if not is_equal:
        #     print(f"{self.initial_unit} to {self.desired_unit}")
        #     print(f"response {approx_student_response}  -  desired {approx_desired_value} \n")
        return is_equal
    
    def is_unit_temp_convertible(self):
        is_convertible = self.initial_unit and self.desired_unit in self.temp_units.keys()
        return is_convertible

    def is_unit_volume_convertible(self):
        is_convertible = self.initial_unit and self.desired_unit in self.vol_units.keys()
        return is_convertible

    def response(self, is_correct):
        if is_correct:
                return "correct"
        else:
            return "incorrect"

    def convert(self):
        if self.is_unit_temp_convertible():
            desired_value = self.convert_temperature()
            is_correct = self.compare_answer(desired_value)
            return self.response(is_correct)

        elif self.is_unit_volume_convertible():
            desired_value = self.convert_volume()
            is_correct = self.compare_answer(desired_value)
            return self.response(is_correct)
            
        else:
            return "Invalid"