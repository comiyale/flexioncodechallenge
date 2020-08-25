from django.test import TestCase

from ..models import UnitType, Unit




# class TestModels(TestCase):
#     def setUp(self):
#         UnitType.objects.create(name='volume')
#         Unit.objects.create(name='liters')

#     def test_unittypemodel_creation(self):
#         volume = UnitType.objects.get(name='volume')
#         # temperature = UnitType.objects.get(name='temperature')
#         self.assertTrue(isinstance(volume, UnitType))
#         # self.assertTrue(isinstance(temperature, UnitType))

#     # def test_unittype_str(self):
#     #     volume = UnitType.objects.get(name='volume')
#     #     # temperature = UnitType.objects.get(name='temperature')
#     #     self.assertEqual(str(volume), 'volume')
#     #     # self.assertEqual(str(temperature), 'temperature')

#     def test_unitmodel_creation(self):
#         liters = Unit.objects.get(name='liters')
#     #     celsius = Unit.objects.get(name='celsius', unit_type=1)
#         self.assertTrue(isinstance(liters, Unit))
#     #     self.assertTrue(isinstance(celsius, Unit))
