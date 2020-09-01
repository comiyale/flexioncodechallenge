import unittest

from convert import Converter


class TemperatureConversionTestCases(unittest.TestCase):
    def test_celcius_to_Kelvin(self):
        self.assertEqual(str(Converter(value=100, initial_unit='Celsius', desired_unit='Kelvin', student_response=373.1)), 'correct')

    def test_Kelvin_to_Celsius(self):
        self.assertEqual(str(Converter(value=100, initial_unit='Kelvin', desired_unit='Celsius', student_response=-173.1)), 'correct')

    def test_Celsius_to_Rankine(self):
        self.assertEqual(str(Converter(value=100, initial_unit='Celsius', desired_unit='Rankine', student_response=671.7)), 'correct')

    def test_Rankine_to_Celsius(self):
        self.assertEqual(str(Converter(value=100, initial_unit='Rankine', desired_unit='Celsius', student_response=-217.6)), 'correct')
    
    def test_Celsius_to_Fahrenheit(self):
        self.assertEqual(str(Converter(value=100, initial_unit='Celsius', desired_unit='Fahrenheit', student_response=212)), 'correct')

    def test_Fahrenheit_to_Celsius(self):
        self.assertEqual(str(Converter(value=100, initial_unit='Fahrenheit', desired_unit='Celsius', student_response=37.8)), 'correct')


class CupsConversionTestCases(unittest.TestCase):
    def test_cups_to_cups(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cups', desired_unit='cups', student_response=100)), 'correct')

    def test_cups_to_gallon(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cups', desired_unit='gallons', student_response=6.25)), 'correct')

    def test_cups_to_liters(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cups', desired_unit='liters', student_response=23.7)), 'correct')

    def test_cups_to_cubic_feet(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cups', desired_unit='cubic_feet', student_response=0.8)), 'correct')

    def test_cups_to_cubic_inches(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cups', desired_unit='cubic_inches', student_response=1443.8)), 'correct')

    def test_cups_to_tablespoons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cups', desired_unit='tablespoons', student_response=1600)), 'correct')


class GallonConversionTestCases(unittest.TestCase):
    def test_gallon_to_gallon(self):
        self.assertEqual(str(Converter(value=100, initial_unit='gallons', desired_unit='gallons', student_response=100)), 'correct')

    def test_gallon_to_cups(self):
        self.assertEqual(str(Converter(value=100, initial_unit='gallons', desired_unit='cups', student_response=1600)), 'correct')

    def test_gallon_to_liters(self):
        self.assertEqual(str(Converter(value=100, initial_unit='gallons', desired_unit='liters', student_response=378.5)), 'correct')

    def test_gallon_to_cubic_feet(self):
        self.assertEqual(str(Converter(value=100, initial_unit='gallons', desired_unit='cubic_feet', student_response=13.4)), 'correct')

    def test_gallon_to_cubic_inches(self):
        self.assertEqual(str(Converter(value=100, initial_unit='gallons', desired_unit='cubic_inches', student_response=23100)), 'correct')

    def test_gallon_to_tablespoons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='gallons', desired_unit='tablespoons', student_response=25600)), 'correct')


class LitersConversionTestCases(unittest.TestCase):
    def test_liters_to_liters(self):
        self.assertEqual(str(Converter(value=100, initial_unit='liters', desired_unit='liters', student_response=100)), 'correct')

    def test_liters_to_cups(self):
        self.assertEqual(str(Converter(value=100, initial_unit='liters', desired_unit='cups', student_response=422.7)), 'correct')

    def test_liters_to_gallon(self):
        self.assertEqual(str(Converter(value=100, initial_unit='liters', desired_unit='gallons', student_response=26.4)), 'correct')

    def test_liters_to_cubic_feet(self):
        self.assertEqual(str(Converter(value=100, initial_unit='liters', desired_unit='cubic_feet', student_response=3.5)), 'correct')

    def test_liters_to_tablespoons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='liters', desired_unit='tablespoons', student_response=6762.8)), 'correct')

    def test_liters_to_cubic_inches(self):
        self.assertEqual(str(Converter(value=100, initial_unit='liters', desired_unit='cubic_inches', student_response=6102.4)), 'correct')


class CubicInchConversionTestCases(unittest.TestCase):
    def test_cubic_inches_to_cubic_inches(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_inches', desired_unit='cubic_inches', student_response=100)), 'correct')

    def test_cubic_inches_to_cups(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_inches', desired_unit='cups', student_response=6.9)), 'correct')

    def test_cubic_inches_to_liters(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_inches', desired_unit='liters', student_response=1.6)), 'correct')

    def test_cubic_inches_to_gallons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_inches', desired_unit='gallons', student_response=0.4)), 'correct')

    def test_cubic_inches_to_cubic_feet(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_inches', desired_unit='cubic_feet', student_response=0.1)), 'correct')

    def test_cubic_inches_to_tablespoons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_inches', desired_unit='tablespoons', student_response=110.8)), 'correct')


class CubicFeetConversionTestCases(unittest.TestCase):
    def test_cubic_feet_to_cubic_feet(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_feet', desired_unit='cubic_feet', student_response=100)), 'correct')

    def test_cubic_feet_to_cups(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_feet', desired_unit='cups', student_response=11968.8)), 'correct')

    def test_cubic_feet_to_liters(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_feet', desired_unit='liters', student_response=2831.7)), 'correct')

    def test_cubic_feet_to_gallons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_feet', desired_unit='gallons', student_response=748.1)), 'correct')

    def test_cubic_feet_to_cubic_inches(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_feet', desired_unit='cubic_inches', student_response=172800)), 'correct')

    def test_cubic_feet_to_tablespoons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_feet', desired_unit='tablespoons', student_response=191501.3)), 'correct')


class TeaspoonConversionTestCases(unittest.TestCase):
    def test_tablespoons_to_tablespoons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='tablespoons', desired_unit='tablespoons', student_response=100)), 'correct')

    def test_tablespoons_to_cups(self):
        self.assertEqual(str(Converter(value=100, initial_unit='tablespoons', desired_unit='cups', student_response=6.2)), 'correct')

    def test_tablespoons_to_liters(self):
        self.assertEqual(str(Converter(value=100, initial_unit='tablespoons', desired_unit='liters', student_response=1.5)), 'correct')
 
    def test_tablespoons_to_gallons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='tablespoons', desired_unit='gallons', student_response=0.4)), 'correct')

    def test_tablespoons_to_cubic_feet(self):
        self.assertEqual(str(Converter(value=100, initial_unit='tablespoons', desired_unit='cubic_feet', student_response=0.1)), 'correct')
 
    def test_tablespoons_to_cubic_inches(self):
        self.assertEqual(str(Converter(value=100, initial_unit='tablespoons', desired_unit='cubic_inches', student_response=90.2)), 'correct')
