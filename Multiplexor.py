from abc import ABC

from Device import Device


class Multiplexer(Device, ABC):
    def __init__(self, name, mass, price):
        super().__init__(name, mass, price)

    @staticmethod
    def forward_signal() -> None:
        print("Do whatever multiplexer does.")
