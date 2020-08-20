from abc import ABCMeta
from abc import abstractmethod


class Checkbox(metaclass=ABCMeta):
    @abstractmethod
    def paint(self):
        pass


class WinCheckbox(Checkbox):
    def paint(self):
        return "This is a win checkbox"


class MacCheckbox(Checkbox):
    def paint(self):
        return "This is a mac checkbox"
