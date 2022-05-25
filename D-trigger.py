from abc import ABC

from Trigger import Trigger


class DTrigger(Trigger, ABC):
    def __init__(self, name, mass, price):
        super().__init__(name, mass, price)

    def trigger(self) -> None:
        print("Do whatever D-trigger does.")
