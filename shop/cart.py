"""A shopping cart with a running total."""
from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    price: float


@dataclass
class Cart:
    items: list = field(default_factory=list)
    total: float = 0.0

    def add(self, item):
        self.items.append(item)
        self.total = sum(i.price for i in self.items)
