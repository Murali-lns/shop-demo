"""Charge a cart."""


def charge(amount):
    print(f"charging {amount:.2f}")


def checkout(cart):
    charge(cart.total)
    return cart.total
