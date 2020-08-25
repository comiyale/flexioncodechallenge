import json
import pint

from rest_framework import serializers

ureg = pint.UnitRegistry()

class Converter(serializers.Serializer):
    def __init__(self):
        initial_unit = serializers.CharField(required=True)


def convert_temp(value, initial_unit, desired_unit):
    temp_units_quantity = ureg.Quantity

    with open('units.json') as file:
        temp_units = json.load(file)

    initial_value = temp_units_quantity(value, temp_units[initial_unit])
    desired_value = initial_value.to(desired_unit).magnitude
    
    return desired_value

def convert_units(value, initial_unit, desired_unit):
    units_quantity = ureg.Quantity

    units = {
            'liters': ureg.liters,
            'gallons': ureg.gallons,
            'teaspoon': ureg.teaspoon,
            'tablespoon': ureg.tablespoon,
            'cubic_inch': ureg.cubic_inch,
            'cubic_feet': ureg.cubic_feet,
        }

    initial_value = value * units[initial_unit]
    desired_value = initial_value.to(desired_unit).magnitude
    
    return desired_value

def check_compatibility(initial_unit, desired_unit):
    compatible_units = list(ureg.get_compatible_units(initial_unit))
    is_compatible = str(desired_unit) in compatible_units

    return is_compatible

def convert(value, initial_unit, desired_unit, isTemp):
    isCompatible = check_compatibility(initial_unit, desired_unit)

    if isCompatible and isTemp:
        value = convert_temp(value, initial_unit, desired_unit)

    elif isCompatible and not isTemp:
        value = convert_units(value, initial_unit, desired_unit)

    return value