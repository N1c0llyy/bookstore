from decimal import Decimal

from django.test import TestCase

from product.models import Product
from order.models import Order


class OrderModelTest(TestCase):
    def test_create_order(self):
        product = Product.objects.create(
            name="Mouse",
            description="Mouse Gamer",
            price=Decimal("150.00"),
            stock=20
        )

        order = Order.objects.create(
            product=product,
            quantity=2
        )

        self.assertEqual(order.product, product)
        self.assertEqual(order.quantity, 2)
        self.assertEqual(str(order), f"Pedido #{order.id} - Mouse")