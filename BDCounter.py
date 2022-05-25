from abc import ABC

from Counter import Counter


class BDCounter(Counter, ABC):
    def __init__(self, name, mass, price):
        super().__init__(name, mass, price)

    def count(self) -> int:
        k = 0
        while True:
            val = input("Enter whatever\n")
            if val != 0:
                k += 1
            else:
                break
        return k
