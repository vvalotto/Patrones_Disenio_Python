
import sys
"""
Clase Receptor
"""

class Windows:

    def exit(self):
        sys.exit(0)

class Document:

    def __init__(self, filename):
        self.filename = filename
        self.contents = 'Algo'

    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.contents)


"""
Clase Invocador
"""

class ToolbarButton:

    def __init__(self, name, iconname):
        self.name = name
        self.iconname = iconname


    def click(self):
        self.command.execute()

class MenuItem:

    def __init__(self, menu_name, menuitem_name):
        self.menu = menu_name
        self.item = menuitem_name

    def click(self):
        self.command.execute()


class KeyboardShortcut:

    def __init__(self, key, modifier):
        self.key = key
        self.modifier = modifier

    def keypress(self):
        self.command.execute()


"""
Commands
"""

class SaveCommand:

    def __init__(self, document):
        self.document = document

    def execute(self):
        self.document.save()


class ExitCommand:

    def __init__(self, window):
        self.window = window

    def execute(self):
        self.window.exit()

