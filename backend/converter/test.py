import unittest

from converterutil import Converter

class TemperatureTestCase(unittest.TestCase):
        def setUp(self):
                self.conversion = Converter(value=100, initial_unit='celsius', desired_unit='kelvin', student_response=373.15)

        def test_check_class_initialised(self):
                self.assertTrue(isinstance(self.conversion, Converter))

        def test_convert_temp(self):
                self.assertEqual(self.conversion.convert_temp(), self.conversion.student_response)

        def test_is_unit_temp(self):
                self.assertTrue(self.conversion.is_unit_temp())

        def test_compare_answer(self):
                self.assertTrue(self.conversion.compare_answer(self.conversion.student_response))
                

class VolumeTestCase(unittest.TestCase):
        def setUp(self):
                self.conversion = Converter(value=6.25, initial_unit='gallons', desired_unit='cups', student_response=100)

        def test_check_class_initialised(self):
                self.assertTrue(isinstance(self.conversion, Converter))

        def test_convert_volume(self):
                self.assertEqual(self.conversion.convert_volume(), self.conversion.student_response)

        def test_is_unit_temp(self):
                self.assertFalse(self.conversion.is_unit_temp())

        def test_compare_answer(self):
                self.assertTrue(self.conversion.compare_answer(self.conversion.student_response))


class UtilsTestCase(unittest.TestCase):
        def test_approx_to_tenth(self):
                self.assertEqual(Converter.approx_to_tenth(self=None, value=123.454), 123.5)
                self.assertEqual(Converter.approx_to_tenth(self=None, value=123.145), 123.1)
                self.assertEqual(Converter.approx_to_tenth(self=None, value=999.99), 1000)
                self.assertNotEqual(Converter.approx_to_tenth(self=None, value=999.99), 999.9)
                self.assertNotEqual(Converter.approx_to_tenth(self=None, value=123.456), 123.46)
                


if __name__ == '__main__':
    unittest.main()