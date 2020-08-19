from abc import ABCMeta
from abc import abstractmethod


class Button(metaclass=ABCMeta):
    @abstractmethod
    def paint(self):
        pass


class WinButton(Button):
    def paint(self):
        return "This is a win button"


class MacButton(Button):
    def paint(self):
        return "This is a mac button"
