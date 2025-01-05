from imports import *
# from test import aba1, aba2
from aba1 import *

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("setGeometry Example")
    self.setFixedSize(1000, 650)

    tabs = QTabWidget()
    tabs.setTabPosition(QTabWidget.North)
    tabs.setMovable(False)

    tabs.addTab(aba1("Imagens/im1.png"), "aba1")
    # tabs.addTab(aba2('im1.png'), "aba2")
    self.setCentralWidget(tabs)
    # tabs.setParent(self)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
