from imports import *
def sen(x): return np.sin(x)


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

        self.ponteiroLinha = 15

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
        self.dadosX = []
        self.dadosY = []
        self.arquivo = None
        self.timer.start(25)  

    def pararAtualizacao(self):
        self.timer.stop()
    
    def atualizarGrafico(self):
        with open("Dados/dados.csv", mode='r') as self.arquivo:
            self.nomeColunas = self.arquivo.readline().strip().split(',')

            self.arquivo.seek(self.ponteiroLinha, 0)
        

            linha = self.arquivo.readline()

            self.ponteiroLinha += len(linha)+1

            linha = linha.strip().split(',')
            print(linha)

            if linha[0] != '':
                self.dadosX.append(float(linha[0]))
                self.dadosY.append(float(linha[1]))

                self.line.set_data(self.dadosX, self.dadosY)

                self.graficoMostrado.set_xlim(0, 100)
                self.graficoMostrado.set_ylim(-1.5, 1.5)

                self.draw()
            else: 
                print("todos os dados foram lidos")
                self.timer.stop()

    def atualizarTitulo(self, novoTitulo):
        self.graficoMostrado.set_title(novoTitulo, fontsize=16)
        self.draw()

    def atualizarXlabel(self, novoTexto):
        self.graficoMostrado.set_xlabel(novoTexto, fontsize=12)
        self.draw()

    def atualizarYlabel(self, novoTexto):
        self.graficoMostrado.set_ylabel(novoTexto, fontsize=12)
        self.draw()


