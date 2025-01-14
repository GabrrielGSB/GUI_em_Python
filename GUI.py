from imports import *
from aba1 import *
from aba2 import *
from aba3 import *

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("setGeometry Example")
    self.setFixedSize(1000, 500)

    tabs = QTabWidget()
    tabs.setTabPosition(QTabWidget.North)
    tabs.setMovable(False)

    tabs.addTab(aba1("Imagens/im1.png"), "aba1")
    tabs.addTab(aba2("Imagens/im1.png"), "aba2")
    self.setCentralWidget(tabs)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
