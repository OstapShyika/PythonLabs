from abc import ABC

from Counter import Counter


class BinaryCounter(Counter, ABC):
    def __init__(self, name, mass, price):
        super().__init__(name, mass, price)

    def count(self) -> str:
        k = 0
        while True:
            val = input("Enter whatever\n")
            if val != "":
                k += 1
            else:
                break

        return bin(k)
