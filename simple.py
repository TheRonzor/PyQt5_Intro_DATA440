import sys
from datetime import datetime as dt

from PyQt5 import QtWidgets as qtw

class SimpleApp(qtw.QApplication):
    def __init__(self, **kwargs):
        super().__init__([])

        # Add the VerticalHelloBox
        self.main_widget = VerticalHelloBox()

        # Run the application
        self.main_widget.show()
        sys.exit(self.exec_())
        return

class WindowWithVerticalSlots(qtw.QWidget):
    def __init__(self, title: str):
        super().__init__()
        # Make a title for the window
        self.setWindowTitle(title)
        # Create a vertical layout container
        self.my_layout = qtw.QVBoxLayout(self)
        return

class VerticalHelloBox(WindowWithVerticalSlots):
    def __init__(self):
        super().__init__(title='Example Interface using PyQt5')
        self.configure()
        return
    
    def configure(self):
        self.greeting_box = qtw.QLabel(self)
        self.hello_button = qtw.QPushButton('Who are you?', self)
        # Bind the function to the hello_button
        self.hello_button.clicked.connect(self.hello_button_clicked)

        self.my_layout.addWidget(self.greeting_box)
        self.my_layout.addWidget(self.hello_button)
        return
    
    def hello_button_clicked(self):
        name_getter = InputPopup()
        if name_getter.exec_() == qtw.QDialog.Accepted:
            self.greeting_box.setText(f'Hello {name_getter.get_text()}!')
        return
    
class InputPopup(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Who are you?')

        # Text box to enter your name
        self.name_entry = qtw.QLineEdit(self)
        self.ok_button = qtw.QPushButton("Ok", self)
        # When the button is clicked, call a built-in function
        # that lets the app now that the dialog is completed
        self.ok_button.clicked.connect(self.accept)
        
        # Create a vertical layout and add the widgets
        self.my_layout = qtw.QVBoxLayout(self)
        self.my_layout.addWidget(self.name_entry)
        self.my_layout.addWidget(self.ok_button)
        return
    
    def get_text(self) -> str:
        # Get the name that was entered into the text box
        return self.name_entry.text()



if __name__ == '__main__':
    SimpleApp()