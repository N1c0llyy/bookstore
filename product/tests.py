from decimal import Decimal

from django.test import TestCase

from .models import Category, Product


class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(
            name="Eletrônicos"
        )

        self.assertEqual(category.name, "Eletrônicos")
        self.assertEqual(str(category), "Eletrônicos")


class ProductModelTest(TestCase):
    def test_create_product(self):
        category = Category.objects.create(
            name="Eletrônicos"
        )

        product = Product.objects.create(
            category=category,
            name="Notebook",
            description="Notebook Gamer",
            price=Decimal("3500.00"),
            stock=10
        )

        self.assertEqual(product.category, category)
        self.assertEqual(product.name, "Notebook")
        self.assertEqual(str(product), "Notebook")