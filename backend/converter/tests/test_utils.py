import unittest

from convert import Converter


class UtilsTestCase(unittest.TestCase):
        def test_approx_to_tenth(self):
                self.assertEqual(Converter.approx_to_tenth(self=None, value=123.454), 123.5)
                self.assertEqual(Converter.approx_to_tenth(self=None, value=123.145), 123.1)
                self.assertEqual(Converter.approx_to_tenth(self=None, value=999.99), 1000)
                self.assertEqual(Converter.approx_to_tenth(self=None, value=305.15), 305.1)
                self.assertNotEqual(Converter.approx_to_tenth(self=None, value=999.99), 999.9)
                self.assertNotEqual(Converter.approx_to_tenth(self=None, value=123.456), 123.46)

        def test_is_respose_correct(self):
                self.assertEqual(Converter.response(self=None,is_correct=True), "correct")
                self.assertNotEqual(Converter.response(self=None,is_correct=False), "correct")
        
        def test_is_respose_incorrect(self):
                self.assertEqual(Converter.response(self=None,is_correct=False), "incorrect")
                self.assertNotEqual(Converter.response(self=None, is_correct=True), "incorrect") 

        def test_is_input_negative(self):
                self.assertTrue(Converter.is_input_negative(self=None, value=-100))
                self.assertFalse(Converter.is_input_negative(self=None, value=100))     
                self.assertFalse(Converter.is_input_negative(self=None, value=0)) 
                