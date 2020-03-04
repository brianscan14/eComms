from django.test import TestCase
from .models import Product


# Create your tests here.
class ProductTests(TestCase):
    """
    defien the tests to run against our prod models
    """
    def test_str(self):
        test_name = Product(name='A Product')
        self.assertEqual(str(test_name), 'A Product')