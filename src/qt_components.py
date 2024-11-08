from src.globals import *

from PyQt5 import QtWidgets as qtw

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg


class WindowWithVerticalSlots(qtw.QWidget):
    '''
    A window with a title and an empty
    vertical container (QVBoxLayout).
    
    Intended use is to inherit and add
    additional customization
    '''
    def __init__(self, title: str):
        super().__init__()
        
        # Make a title for the window
        self.setWindowTitle(title)
        
        # Create an empty vertical layout container
        self.my_layout = qtw.QVBoxLayout(self)
        return
    
class WindowWithFigureAbove(WindowWithVerticalSlots):
    '''
    A window with vertical layout and matplotlib figure on top.
    '''
    def __init__(self,
                 fig: plt.Figure,
                 title: str = 'Window with a Figure'
                 ):
        super().__init__(title=title)

        # Put the figure into a canvas and add to the layout
        self.canvas = FigureCanvasQTAgg(fig)
        self.my_layout.addWidget(self.canvas)
        return

class ButtonRow(qtw.QHBoxLayout):
    '''
    A horizontal row of buttons. Names must be provided for each.
    '''
    def __init__(self,
                 names: list[str]
                 ):
        super().__init__()

        self.items = []
        for name in names:
            self.items.append(qtw.QPushButton(name))
            self.addWidget(self.items[-1])
        return
    
class ButtonBox(qtw.QVBoxLayout):
    '''
    A vertical container of ButtonRow objects.

        nrows: How many rows of buttons
        ncols: How many buttons per row
    '''
    def __init__(self,
                 nrows: int,
                 ncols: int
                 ):
        super().__init__()

        self.rows = []
        for _ in range(nrows):
            names = [str(n) for n in range(ncols)]
            self.rows.append(ButtonRow(names))
            self.addLayout(self.rows[-1])
        
        return
    
def configure_button(button: qtw.QPushButton,
                     text: str,
                     command: Callable
                     ) -> None:
    button.setText(text)
    button.clicked.connect(command)
    return