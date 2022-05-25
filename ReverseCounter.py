from abc import ABC

from Counter import Counter


class ReverseCounter(Counter, ABC):
    def __init__(self, name, mass, price):
        super().__init__(name, mass, price)

    def count(self) -> None:
        print("Do whatever reverse counter does.")
