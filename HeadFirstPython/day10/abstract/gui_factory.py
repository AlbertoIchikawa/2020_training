from abc import ABCMeta
from abc import abstractmethod

from day10.abstract.button import WinButton, MacButton
from day10.abstract.checkbox import WinCheckbox, MacCheckbox


class GUIFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WinFactory(GUIFactory):
    def __init__(self):
        print("This is WinFactory")

    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()


class MacFactory(GUIFactory):
    def __init__(self):
        print("This is MacFactory")

    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()
