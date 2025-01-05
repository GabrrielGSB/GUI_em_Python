from imports import *

class definirPlanoDeFundo(QWidget):
    def __init__(self, caminho):
        super().__init__()
        self.caminho = caminho

    def paintEvent(self, event):
        painter      = QPainter(self)
        planoDeFundo = QPixmap(self.caminho) 
        painter.drawPixmap(0, 0, self.width(), self.height(), planoDeFundo)
