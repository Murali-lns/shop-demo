import unittest

from shop.cart import Cart, Item


class CartTest(unittest.TestCase):
    def test_total_is_sum_of_items(self):
        cart = Cart()
        cart.add(Item("mug", 10.0))
        cart.add(Item("pen", 2.5))
        self.assertEqual(cart.total, 12.5)


if __name__ == "__main__":
    unittest.main()
