import unittest

from convert import Converter


class ResultTestCases(unittest.TestCase):
    def test_result_is_invalidd(self):
        self.assertEqual(str(Converter(value=73.12, initial_unit='gallons', desired_unit='Kelvin', student_response=19.4)), 'invalid')
        self.assertEqual(str(Converter(value=200, initial_unit='Celsius', desired_unit='cups', student_response=19.4)), 'invalid')
        self.assertEqual(str(Converter(value=180.12, initial_unit='Kelvin', desired_unit='tablespoons', student_response=19.4)), 'invalid')
        self.assertEqual(str(Converter(value=-750.12, initial_unit='gallons', desired_unit='Kelvin', student_response=19.4)), 'invalid')
        self.assertEqual(str(Converter(value=-100, initial_unit='Kelvin', desired_unit='cups', student_response=19.4)), 'invalid') 
        self.assertEqual(str(Converter(value=34, initial_unit='dog', desired_unit='cups', student_response=86)), 'invalid')
        self.assertEqual(str(Converter(value=-25, initial_unit='Kelvin', desired_unit='cats', student_response=19.4)), 'invalid') 


    def test_result_is_incorrect(self):
        self.assertEqual(str(Converter(value=42, initial_unit='Kelvin', desired_unit='Celsius', student_response=874)), 'incorrect')
        self.assertEqual(str(Converter(value=90, initial_unit='Fahrenheit', desired_unit='Celsius', student_response=38.2)), 'incorrect')
        self.assertEqual(str(Converter(value=1.23, initial_unit='Kelvin', desired_unit='Rankine', student_response=34.2)), 'incorrect')
        self.assertEqual(str(Converter(value=54.54, initial_unit='gallons', desired_unit='liters', student_response=84.1)), 'incorrect')
        self.assertEqual(str(Converter(value=45, initial_unit='cups', desired_unit='gallons', student_response=0)), 'incorrect')
        self.assertEqual(str(Converter(value=-839, initial_unit='Kelvin', desired_unit='Celsius', student_response=89.93)), 'incorrect')
        