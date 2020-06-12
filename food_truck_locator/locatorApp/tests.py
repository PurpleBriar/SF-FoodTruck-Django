from django.test import TestCase

# Create your tests here.

from .models import FoodTruckInfo

class FoodTruckInfoTestCase(TestCase):
    def setUp(self):
        FoodTruckInfo.objects.create(name="Test Tacos", address="341 S. Main Street", foodItems="Tacos", latitude="37.4", longitude="-122.4")

    def test_basic_instance_creation(self):
        """Animals that can speak are correctly identified"""
        tacoTruck = FoodTruckInfo.objects.get(name="Test Tacos")
        self.assertEqual(str(tacoTruck), 'Test Tacos at 341 S. Main Street')