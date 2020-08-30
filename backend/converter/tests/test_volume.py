import unittest

from convert import Converter


class VolumeTestCase(unittest.TestCase):
        def setUp(self):
                self.conversion = Converter(value=6.25, initial_unit='gallons', desired_unit='cup', student_response=100)

        def test_check_class_initialised(self):
                self.assertTrue(isinstance(self.conversion, Converter))

        def test_convert_volume(self):
                self.assertEqual(self.conversion.convert_volume(), self.conversion.student_response)

        def test_is_unit_volume_convertible(self):
                self.assertTrue(self.conversion.is_unit_volume_convertible())

        def test_is_not_temperature_unit(self):
                self.assertFalse(self.conversion.is_unit_temp_convertible())

        def test_compare_answer(self):
                self.assertTrue(self.conversion.compare_answer(self.conversion.student_response))
