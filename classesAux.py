from imports import *

class definirPlanoDeFundo(QWidget):
    def __init__(self, caminho):
        super().__init__()
        self.caminho = caminho

    def paintEvent(self, event):
        painter      = QPainter(self)
        planoDeFundo = QPixmap(self.caminho) 
        painter.drawPixmap(0, 0, self.width(), self.height(), planoDeFundo)

class JanelaGrafico(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfico Externo")
        self.setGeometry(100, 100, 800, 600)

        # Criação do gráfico usando Matplotlib
        self.grafico = Grafico(self)
        self.setCentralWidget(self.grafico)

class Grafico(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure(figsize=(8, 6), dpi=100)
        super().__init__(self.fig)

        self.graficoMostrado = self.fig.add_subplot(111)

        #Cria o timer que vai controlar a taxa de atualização do gráfico e a função atrelada
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizarGrafico)

        self.graficoMostrado.set_title("Gráfico", fontsize=16)
        self.graficoMostrado.set_xlabel("Eixo X", fontsize=12)
        self.graficoMostrado.set_ylabel("Eixo Y", fontsize=12)
        self.graficoMostrado.grid()
        self.line, = self.graficoMostrado.plot([], [], label="Dados", color="blue", linewidth=1)
        self.graficoMostrado.legend()
       
    def iniciarAtualizacao(self):
        self.x_data = []
        self.y_data = []
        self.timer.start(100)  

    def pararAtualizacao(self):
        self.timer.stop()
    
    def atualizarGrafico(self):
        if len(self.x_data) > 100:  # Limita o número de pontos no gráfico
            self.x_data.pop(0)
            self.y_data.pop(0)

        novo_x = (self.x_data[-1] + 0.1) if self.x_data else 0
        novo_y = sen(novo_x)
        
        self.x_data.append(novo_x)
        self.y_data.append(novo_y)

        # Atualiza a linha do gráfico
        self.line.set_data(self.x_data, self.y_data)
        self.graficoMostrado.set_xlim(max(0, novo_x - 50), novo_x + 1)
        self.graficoMostrado.set_ylim(-1.5, 1.5)

        self.draw()

    def atualizarTitulo(self, novoTitulo):
        self.graficoMostrado.set_title(novoTitulo, fontsize=16)
        self.draw()

    def atualizarXlabel(self, novoTexto):
        self.graficoMostrado.set_xlabel(novoTexto, fontsize=12)
        self.draw()

    def atualizarYlabel(self, novoTexto):
        self.graficoMostrado.set_ylabel(novoTexto, fontsize=12)
        self.draw()

