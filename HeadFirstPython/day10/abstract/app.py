import json
import os
from day10.abstract.gui_factory import GUIFactory, WinFactory, MacFactory

CONFIG_FILE_NAME = "app_config.json"


class Application:
    def __init__(self, gui_factory: GUIFactory):
        self.factory = gui_factory
        self.button = None
        self.checkbox = None

    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def paint(self):
        print(self.button.paint())
        print(self.checkbox.paint())


def read_app_config_file():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_file_path = os.path.join(dir_path, CONFIG_FILE_NAME)
    with open(config_file_path) as config_file:
        return json.load(config_file)


if __name__ == "__main__":
    config = read_app_config_file()
    if config['os'] == "Windows":
        factory = WinFactory()
    elif config['os'] == "Mac":
        factory = MacFactory()
    else:
        raise Exception("Error! Unknown operating system.")

    app = Application(factory)
    app.create_ui()
    app.paint()
