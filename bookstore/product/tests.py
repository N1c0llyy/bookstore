from decimal import Decimal

from django.test import TestCase

from .models import Product


class ProductModelTest(TestCase):
    def test_create_product(self):
        product = Product.objects.create(
            name="Notebook",
            description="Notebook Gamer",
            price=Decimal("3500.00"),
            stock=10
        )

        self.assertEqual(product.name, "Notebook")
        self.assertEqual(product.description, "Notebook Gamer")
        self.assertEqual(product.price, Decimal("3500.00"))
        self.assertEqual(product.stock, 10)
        self.assertEqual(str(product), "Notebook")