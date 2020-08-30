import unittest

from convert import Converter


class TemperatureConversionTestCases(unittest.TestCase):
    def test_celcius_to_kelvin(self):
        self.assertEqual(str(Converter(value=100, initial_unit='celsius', desired_unit='kelvin', student_response=373.1)), 'correct')

    def test_kelvin_to_celsius(self):
        self.assertEqual(str(Converter(value=100, initial_unit='kelvin', desired_unit='celsius', student_response=-173.1)), 'correct')

    def test_celsius_to_rankine(self):
        self.assertEqual(str(Converter(value=100, initial_unit='celsius', desired_unit='rankine', student_response=671.7)), 'correct')

    def test_rankine_to_celsius(self):
        self.assertEqual(str(Converter(value=100, initial_unit='rankine', desired_unit='celsius', student_response=-217.6)), 'correct')
    
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(str(Converter(value=100, initial_unit='celsius', desired_unit='fahrenheit', student_response=212)), 'correct')

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(str(Converter(value=100, initial_unit='fahrenheit', desired_unit='celsius', student_response=37.8)), 'correct')


class CupConversionTestCases(unittest.TestCase):
    def test_cup_to_cup(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cup', desired_unit='cup', student_response=100)), 'correct')

    def test_cup_to_gallon(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cup', desired_unit='gallons', student_response=6.25)), 'correct')

    def test_cup_to_liters(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cup', desired_unit='liters', student_response=23.7)), 'correct')

    def test_cup_to_teaspoons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cup', desired_unit='teaspoons', student_response=4800)), 'correct')

    def test_cup_to_cubic_inch(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cup', desired_unit='cubic_inch', student_response=1443.8)), 'correct')

    def test_cup_to_tablespoon(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cup', desired_unit='tablespoon', student_response=1600)), 'correct')


class GallonConversionTestCases(unittest.TestCase):
    def test_gallon_to_gallon(self):
        self.assertEqual(str(Converter(value=100, initial_unit='gallons', desired_unit='gallons', student_response=100)), 'correct')

    def test_gallon_to_cup(self):
        self.assertEqual(str(Converter(value=100, initial_unit='gallons', desired_unit='cup', student_response=1600)), 'correct')

    def test_gallon_to_liters(self):
        self.assertEqual(str(Converter(value=100, initial_unit='gallons', desired_unit='liters', student_response=378.5)), 'correct')

    def test_gallon_to_teaspoons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='gallons', desired_unit='teaspoons', student_response=76800)), 'correct')

    def test_gallon_to_cubic_inch(self):
        self.assertEqual(str(Converter(value=100, initial_unit='gallons', desired_unit='cubic_inch', student_response=23100)), 'correct')

    def test_gallon_to_tablespoon(self):
        self.assertEqual(str(Converter(value=100, initial_unit='gallons', desired_unit='tablespoon', student_response=25600)), 'correct')


class LitersConversionTestCases(unittest.TestCase):
    def test_liters_to_liters(self):
        self.assertEqual(str(Converter(value=100, initial_unit='liters', desired_unit='liters', student_response=100)), 'correct')

    def test_liters_to_cup(self):
        self.assertEqual(str(Converter(value=100, initial_unit='liters', desired_unit='cup', student_response=422.7)), 'correct')

    def test_liters_to_gallon(self):
        self.assertEqual(str(Converter(value=100, initial_unit='liters', desired_unit='gallons', student_response=26.4)), 'correct')

    def test_liters_to_teaspoon(self):
        self.assertEqual(str(Converter(value=100, initial_unit='liters', desired_unit='teaspoons', student_response=20288.4)), 'correct')

    def test_liters_to_tablespoon(self):
        self.assertEqual(str(Converter(value=100, initial_unit='liters', desired_unit='tablespoon', student_response=6762.8)), 'correct')

    def test_liters_to_cubic_inch(self):
        self.assertEqual(str(Converter(value=100, initial_unit='liters', desired_unit='cubic_inch', student_response=6102.4)), 'correct')


class CubicInchConversionTestCases(unittest.TestCase):
    def test_cubic_inch_to_cubic_inch(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_inch', desired_unit='cubic_inch', student_response=100)), 'correct')

    def test_cubic_inch_to_cup(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_inch', desired_unit='cup', student_response=6.9)), 'correct')

    def test_cubic_inch_to_liters(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_inch', desired_unit='liters', student_response=1.6)), 'correct')

    def test_cubic_inch_to_gallons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_inch', desired_unit='gallons', student_response=0.4)), 'correct')

    def test_cubic_inch_to_teaspoons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_inch', desired_unit='teaspoons', student_response=332.5)), 'correct')

    def test_cubic_inch_to_tablespoon(self):
        self.assertEqual(str(Converter(value=100, initial_unit='cubic_inch', desired_unit='tablespoon', student_response=110.8)), 'correct')


class TablespoonConversionTestCases(unittest.TestCase):
    def test_teaspoons_to_teaspoons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='teaspoons', desired_unit='teaspoons', student_response=100)), 'correct')

    def test_teaspoons_to_cup(self):
        self.assertEqual(str(Converter(value=100, initial_unit='teaspoons', desired_unit='cup', student_response=2.1)), 'correct')

    def test_teaspoons_to_liters(self):
        self.assertEqual(str(Converter(value=100, initial_unit='teaspoons', desired_unit='liters', student_response=0.5)), 'correct')

    def test_teaspoons_to_gallons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='teaspoons', desired_unit='gallons', student_response=0.1)), 'correct')

    def test_teaspoons_to_cubic_inch(self):
        self.assertEqual(str(Converter(value=100, initial_unit='teaspoons', desired_unit='cubic_inch', student_response=30.1)), 'correct')

    def test_teaspoons_to_tablespoon(self):
        self.assertEqual(str(Converter(value=100, initial_unit='teaspoons', desired_unit='tablespoon', student_response=33.3)), 'correct')


class TeaspoonConversionTestCases(unittest.TestCase):
    def test_tablespoon_to_tablespoon(self):
        self.assertEqual(str(Converter(value=100, initial_unit='tablespoon', desired_unit='tablespoon', student_response=100)), 'correct')

    def test_tablespoon_to_cup(self):
        self.assertEqual(str(Converter(value=100, initial_unit='tablespoon', desired_unit='cup', student_response=6.2)), 'correct')

    def test_tablespoon_to_liters(self):
        self.assertEqual(str(Converter(value=100, initial_unit='tablespoon', desired_unit='liters', student_response=1.5)), 'correct')
 
    def test_tablespoon_to_gallons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='tablespoon', desired_unit='gallons', student_response=0.4)), 'correct')

    def test_tablespoon_to_teaspoons(self):
        self.assertEqual(str(Converter(value=100, initial_unit='tablespoon', desired_unit='teaspoons', student_response=300)), 'correct')
 
    def test_tablespoon_to_cubic_inch(self):
        self.assertEqual(str(Converter(value=100, initial_unit='tablespoon', desired_unit='cubic_inch', student_response=90.2)), 'correct')
