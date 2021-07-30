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

        # calling the Ui_Components method 
        self.Ui_Components()

    def Ui_Components(self):

        # creating a widget object
        widget = QWidget()

        # text
        text = "Different Symbols"
        # creating a label
        label = QLabel(text)

        # y values to plot by line 1
        y = [2, 8, 6, 8, 6, 11, 14, 13, 18, 19]
        # y values to plot by line 2
        y2 = [3, 1, 5, 8, 9, 11, 16, 17, 14, 16]
        x = range(0, 10)

         # create plot window object
        plt = pg.plot()

        line1 = plt.plot(x, y, pen ='g', symbol ='x', symbolPen ='r', symbolBrush = 0.2, name ='green')
  
        line2 = plt.plot(x, y2, pen ='b', symbol ='o', symbolPen ='b', symbolBrush = 0.2, name ='blue')

        # setting symbol size
        line1.setSymbolSize(45)

        # showing x and y grids
        plt.showGrid(x = True, y = True)

        # set properties of the label for y axis
        plt.setLabel('left', 'Vertical Values', units ='y')
  
        # set properties of the label for x axis
        plt.setLabel('bottom', 'Horizontal Vlaues', units ='s')

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

