from abc import ABC

from Device import Device


class ShiftRegister(Device, ABC):
    def __init__(self, name, mass, price):
        super().__init__(name, mass, price)

    @staticmethod
    def forward_signal() -> None:
        print("Do whatever shift register does.")