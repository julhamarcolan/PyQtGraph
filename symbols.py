import sys 
import numpy as np
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from collections import namedtuple

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting window title
        self.setWindowTitle("PyQt Graph")
        # setting window  geometry
        self.setGeometry(100, 100, 800, 500)

        # calling method
        self.Ui_components()
  
        # showing all the widgets
        self.show()

    def Ui_components(self):

        # creating a widget object
        widget = QWidget()

        # text
        text = "Different Symbols"

        # creating a label
        label = QLabel(text)

        # creating a plot window
        plot = pg.plot()
  
        # adding legend to the plot window
        plot.addLegend()

        # pen = color of the line, symbolBlush = color of the symbol
        # plot the line1 with symbol o
        # having color blue
        line1 = plot.plot([1, 1, 1, 1, 1], pen =(0, 0, 200), symbolBrush =(0, 0, 200),
                          symbolPen ='w', symbol ='o', symbolSize = 14, name ="symbol ='o'")

        line2 = plot.plot([2,2,2,2,2], pen = (0,200,0), symbolBrush =(0, 200, 0),
                          symbolPen ='w', symbol ='t', symbolSize = 14, name ="symbol ='t'" )
        
        line3 = plot.plot([3, 3, 3, 3, 3], pen =(19, 234, 201), symbolBrush =(19, 234, 201),
                          symbolPen ='w', symbol ='t1', symbolSize = 14, name ="symbol ='t1'")

        line4 = plot.plot([4, 4, 4, 4, 4], pen =(195, 46, 212), symbolBrush =(195, 46, 212),
                          symbolPen ='w', symbol ='t2', symbolSize = 14, name ="symbol ='t2'")
  
        line5 = plot.plot([5, 5, 5, 5, 5], pen =(250, 194, 5), symbolBrush =(250, 194, 5),
                          symbolPen ='w', symbol ='t3', symbolSize = 14, name ="symbol ='t3'")
  
        line6 = plot.plot([6, 6, 6, 6, 6], pen =(54, 55, 55), symbolBrush =(55, 55, 55), symbolPen ='w', 
                        symbol ='s', symbolSize = 14, name ="symbol ='s'")
  
        line7 = plot.plot([7, 7, 7, 7, 7], pen =(0, 114, 189), symbolBrush =(0, 114, 189),
                         symbolPen ='w', symbol ='p', symbolSize = 14, name ="symbol ='p'")
  
        line8 = plot.plot([8, 8, 8, 8, 8], pen =(217, 83, 25), symbolBrush =(217, 83, 25),
                          symbolPen ='w', symbol ='h', symbolSize = 14, name ="symbol ='h'")
  
        line9 = plot.plot([9, 9, 9, 9, 9], pen =(237, 177, 32), symbolBrush =(237, 177, 32),
                          symbolPen ='w', symbol ='star', symbolSize = 14, name ="symbol ='star'")

        line10 = plot.plot([10, 10, 10, 10, 10], pen =(126, 47, 142), symbolBrush =(126, 47, 142),
                           symbolPen ='w', symbol ='+', symbolSize = 14, name ="symbol ='+'")
  
        line11 = plot.plot([11, 11, 11, 11, 11], pen =(119, 172, 48), symbolBrush =(119, 172, 48),
                           symbolPen ='w', symbol ='d', symbolSize = 14, name ="symbol ='d'")
  
        line12 = plot.plot([12, 12, 12, 12, 12], pen =(180, 180, 180), symbolBrush =(180, 180, 180),
                           symbolPen ='w', symbol ='x', symbolSize = 14, name ="symbol ='x'")

        # setting x-axis range
        plot.setXRange(-3, 4)
        
        # Creating a grid layout
        layout = QGridLayout()

        # setting this layout to the widget
        widget.setLayout(layout)

        layout.addWidget(plot)

        layout.addWidget(label)
        
        # setting this widget as central widget of the main widow
        self.setCentralWidget(widget)
  
  


# main method
if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec_())