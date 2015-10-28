Simple Shopping Cart
====================

Simple Shopping Cart, ideal for use with Django.

Created as a simple thought exercise on a lonely Friday evening. Could be suitable for use in production, but it was
more about me learning list comprehension and generators a few years ago.

The most recent updates were about handling Python 3.


Tested versions
---------------

- Python 2.7.9
- Python 3.3.5
- Python 3.4.2
- Python 3.5.0

.. image:: https://travis-ci.org/danux/shopping_cart.svg?branch=master
    :target: https://travis-ci.org/danux/shopping_cart


How to use
----------

Cart takes any generic product - could be a Django model, could be anything.
The product must have two attributes at the very least::

product_id
  integer
price
  float/integer

::

    class Product(object):
        def __init__(self, product_id, price):
            self.product_id = int(product_id)
            self.price = float(price)

::

    # Initialising
    from cart import Cart
    cart = Cart()

    # Adding products
    cart.add_product(product)  # Add product
    cart.add_product(product, 5)  # Add product, with a quantity for 5

    # Updating products
    cart.update_quantity(product, 5)  # Adjust the quantity of a product
    cart.remove_product(product)  # Remove a product

    # You can also view some info about the cart
    cart.num_items()  # Sum of all item's quantities in the cart
    cart.sub_total()  # Sum of all product's prices

    # You can also save to a Django session
    cart.save(self.request.session)


Tests
-----

See test.py for full usage

Note: Mock must be installed to run UnitTests on Python 2.7
