# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cart import Cart, CartError
try:
    from unittest.mock import NonCallableMock
except ImportError:
    from mock import NonCallableMock
import unittest


class CartTestCase(unittest.TestCase):

    def setUp(self):
        self.session = {}
        self.product_one = NonCallableMock(product_id=1, price=1.99)
        self.product_two = NonCallableMock(product_id=2, price=2.49)
        self.cart = Cart(self.session)

    def test_can_add_product(self):
        self.cart.add_product(self.product_one, 10)
        self.assertEqual(self.cart.get_cart_item(self.product_one).quantity, 10)

    def test_cannot_add_product_twice(self):
        self.cart.add_product(self.product_one, 13)
        self.assertRaises(CartError, lambda: self.cart.add_product(self.product_one, 10))

    def test_remove_product(self):
        self.cart.add_product(self.product_one, 10)
        self.cart.remove_product(self.product_one)
        self.assertEqual(self.cart.num_items, 0)
        self.assertRaises(CartError, lambda: self.cart.get_cart_item(self.product_one))

    def test_cannot_remove_product_not_in_cart(self):
        self.assertRaises(CartError, lambda: self.cart.remove_product(self.product_one))

    def test_can_calculate_quantity_of_cart(self):
        self.cart.add_product(self.product_one, 10)
        self.assertEqual(self.cart.num_items, 10)
        self.cart.add_product(self.product_two, 15)
        self.assertEqual(self.cart.num_items, 25)

    def test_quantity_of_empty_cart_is_zero(self):
        self.assertEqual(self.cart.num_items, 0)

    def test_can_calculate_subtotal_of_cart(self):
        self.cart.add_product(self.product_one, 10)
        self.assertEqual(self.cart.sub_total, 19.9)
        self.cart.add_product(self.product_two, 15)
        self.assertEqual(self.cart.sub_total, 57.25)

    def test_subtotal_of_empty_cart_is_zero(self):
        self.assertEqual(self.cart.sub_total, 0)

    def test_can_update_quanity(self):
        self.cart.add_product(self.product_one, 10)
        self.cart.update_quantity(self.product_one, 15)
        self.assertEqual(self.cart.get_cart_item(self.product_one).quantity, 15)

    def test_cannot_update_quantity_if_not_in_cart(self):
        self.assertRaises(CartError, lambda: self.cart.update_quantity(self.product_one, 10))

    def test_can_save_cart(self):
        self.cart.add_product(self.product_one)
        self.cart.save(self.session)
        self.new_cart = Cart(self.session)
        self.assertEqual(self.cart.cart_items, self.new_cart.cart_items)

    def test_can_reset_cart(self):
        self.cart.add_product(self.product_one, 10)
        self.cart.reset()
        self.assertEqual(self.cart.cart_items, [])


if __name__ == '__main__':
    unittest.main()
