from abc import ABC, abstractmethod


class Device(ABC):

    def __init__(self, name: str, mass: int, price: int) -> None:
        self._mass = mass
        self._price = price
        self._name = name

    def __str__(self):
        return f"Device-{self.name}[mass: {self.mass}, price: {self._price}]"



