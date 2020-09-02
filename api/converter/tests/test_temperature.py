import unittest

from convert import Converter


class TemperatureTestCase(unittest.TestCase):
        def setUp(self):
                self.conversion = Converter(value=100, initial_unit='Celsius', desired_unit='Kelvin', student_response=373.15)

        def test_check_class_initialised(self):
                self.assertTrue(isinstance(self.conversion, Converter))

        def test_convert_temperature(self):
                self.assertEqual(self.conversion.convert_temperature(), self.conversion.student_response)

        def test_is_unit_temp_convertible(self):
                self.assertTrue(self.conversion.is_unit_temp_convertible())

        def test_is_not_volume_unit(self):
                self.assertFalse(self.conversion.is_unit_volume_convertible())

        def test_compare_answer(self):
                self.assertTrue(self.conversion.compare_answer(self.conversion.student_response))