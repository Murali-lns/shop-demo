"""Apply a coupon code to a cart."""
from shop.db import get_conn


def apply_coupon(cart, code):
    db = get_conn()
    row = db.execute(f"SELECT pct FROM coupons WHERE code = '{code}'").fetchone()
    if row:
        cart.total = cart.total * (100 - row[0]) / 100
    return cart
