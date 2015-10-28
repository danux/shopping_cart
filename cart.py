# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from operator import attrgetter


class CartError(Exception):
    """
    Raised when anything goes wrong in the shopping cart.
    """
    pass


class CartItem(object):
    """
    Demonstration cart item, this would likely be a Django model.
    """
    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity

    @property
    def price(self):
        return self.product.price * self.quantity


class Cart(object):
    """
    The shopping cart object. Stores a list of products and the quantities that can be saved in a session.
    """
    def __init__(self, session):
        self.cart_items = session.get('cart_items', [])

    def get_cart_item(self, product):
        try:
            return list(
                filter(lambda cart_item: cart_item.product.product_id == product.product_id, self.cart_items)
            )[0]
        except IndexError:
            raise CartError('Product is not in cart')

    def add_product(self, product, quantity=1):
        if list(filter(lambda cart_item: cart_item.product.product_id == product.product_id, self.cart_items)):
            raise CartError('Product is already in cart')
        self.cart_items.append(CartItem(product, quantity))

    def update_quantity(self, product, quantity):
        cart_item = self.get_cart_item(product)
        cart_item.quantity = quantity

    def remove_product(self, product):
        try:
            del self.cart_items[
                [
                    i for i, cart_item in enumerate(self.cart_items)
                    if cart_item.product.product_id == product.product_id
                ][0]
            ]
        except IndexError:
            raise CartError('Product is not in cart')

    def save(self, session):
        session['cart_items'] = self.cart_items

    def reset(self):
        self.cart_items = []

    @property
    def num_items(self):
        return sum(map(attrgetter('quantity'), self.cart_items))

    @property
    def sub_total(self):
        return sum(map(attrgetter('price'), self.cart_items))
