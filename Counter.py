from abc import abstractmethod, ABC

from Device import Device


class Counter(Device, ABC):

    def __init__(self, name, mass, price):
        super().__init__(name, mass, price)

    @abstractmethod
    def count(self):
        pass
