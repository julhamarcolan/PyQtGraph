from PyQt5.QtWidgets import *
import pyqtgraph as pg
from PyQt5.QtGui import *
import sys 

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
 
        # creating a new label
        label = QLabel("Line Plot")

        # y values to plot by line 1
        y = [2, 8, 6, 8, 6, 11, 14, 13, 18, 19]
 
        # y values to plot by line 2
        y2 = [3, 1, 5, 8, 9, 11, 16, 17, 14, 16]
        x = range(0, 10)
 
        # create plot window object
        plt = pg.plot()

        # showing x and y grids
        plt.showGrid(x = True, y = True)

        # setting horizontal range
        plt.setXRange(0, 10)
 
        # setting vertical range
        plt.setYRange(0, 20)

        # ploting line in green color
        # with dot symbol as x, not a mandatory field
        line1 = plt.plot(x, y, pen ='g', symbol ='x', symbolPen ='g', symbolBrush = 0.2, name ='green')
 
        # ploting line2 with blue color
        # with dot symbol as o
        line2 = plt.plot(x, y2, pen ='b', symbol ='o', symbolPen ='b', symbolBrush = 0.2, name ='blue')

        # setting alpha value of the line 1
        line1.setAlpha(2.0, True)

        # setting alpha value of the line 2
        line2.setAlpha(0.5, True)

        layout = QGridLayout()

        widget.setLayout(layout)

        layout.addWidget(plt)

        layout.addWidget(label)

        self.setCentralWidget(widget)

 
# main method
if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec_())
