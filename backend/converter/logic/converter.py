import json
import pint

from rest_framework import serializers

ureg = pint.UnitRegistry()

class Converter:
    def __init__(self, value, initial_unit, desired_unit, isTemp=False):
        self.value = value
        self.isTemp = isTemp
        self.initial_unit = initial_unit
        self.desired_unit = desired_unit

    def convert_temp(self):
        temp_units_quantity = ureg.Quantity
        
        temp_units = {
            "kelvin": ureg.kelvin,
            "rankine": ureg.rankine,
            "celsius": ureg.celsius,
            "fahrenheit": ureg.fahrenheit
        }

        initial_value = temp_units_quantity(self.value, temp_units[self.initial_unit])
        print(type(temp_units[self.initial_unit]))
        desired_value = initial_value.to(self.desired_unit).magnitude
        
        return desired_value

    def convert_units(self):
        # units_quantity = ureg.Quantity

        units = {
                'liters': ureg.liters,
                'gallons': ureg.gallons,
                'teaspoon': ureg.teaspoon,
                'tablespoon': ureg.tablespoon,
                'cubic_inch': ureg.cubic_inch,
                'cubic_feet': ureg.cubic_feet,
            }

        initial_value = self.value * units[self.initial_unit]
        desired_value = initial_value.to(self.desired_unit).magnitude
        
        return desired_value

    def check_compatibility(self):
        compatible_units = list(ureg.get_compatible_units(self.initial_unit))
        is_compatible = str(self.desired_unit) in compatible_units

        return is_compatible

    def convert(self):
        isCompatible = self.check_compatibility()

        if self.isTemp:
            return self.convert_temp()
            
        elif isCompatible and not self.isTemp:
            return self.convert_units()     
        
        else:
            return "Not Working"