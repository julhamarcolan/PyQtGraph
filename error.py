import sys 
import numpy as np
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QMainWindow): 
    def __init__(self):
        super().__init__()

        # setting window title
        self.setWindowTitle("PyQt Graph")
        # setting window  geometry
        self.setGeometry(100, 100, 800, 500)

        #calling the Ui_Componets method
        self.Ui_Componets()

    def Ui_Componets(self):
        
        # creating a widget object
        widget = QWidget()

        # text
        text = "Error Bar"
        # creating a label
        label = QLabel(text)

        # create plot window object
        plt = pg.plot()

        # creating x-axis values
        x = np.arange(10)
  
        # creating y-axis values
        y = np.arange(10) % 3
  
        # creating upper bound values
        top = np.linspace(1.0, 3.0, 10)
  
        # creating lower bound values
        bottom = np.linspace(2, 0.5, 10)

        # creating a error bar item
        error = pg.ErrorBarItem(x=x, y=y, top=top, bottom=bottom, beam=0.5)
  
        # adding error bar item to the plot window
        plt.addItem(error)

        # plotting the data on plot window
        plt.plot(x, y, symbol='o', pen={'color': 0.8, 'width': 2})

        
        # showing x and y grids
        plt.showGrid(x = True, y = True)

        #Creating the layout 
        layout = QGridLayout()

        # setting this layout to the widget
        widget.setLayout(layout)

        # Adding the plot to the layout 
        layout.addWidget(plt)

        #Add the label to the layout
        layout.addWidget(label)

        # setting this widget as central widget of the main widow
        self.setCentralWidget(widget)

# main method
if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec_())



