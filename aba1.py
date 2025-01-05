from imports import *
from classesAux import *

maquinas = ["maquina1", "maquina2", "maquina3"]

class aba1(QWidget):
    def __init__(self, imagemFundo):
        super().__init__()

        self.imagemFundo = imagemFundo

        self.planoDeFundo = definirPlanoDeFundo(self.imagemFundo)
        self.planoDeFundo.setGeometry(0, 0, self.width(), self.height())

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0) 
        self.layout.addWidget(self.planoDeFundo)

        self.Selecao = QComboBox()
        self.Selecao.move(50,150)
        self.Selecao.setFixedSize(380, 30)
        self.Selecao.addItems([maquinas[0], maquinas[1], maquinas[2]])
        # self.Selecao.currentIndexChanged.connect(self.index_changed)
        self.Selecao.currentTextChanged.connect(self.atualizarImagem)
        self.Selecao.setParent(self.planoDeFundo)
        self.Selecao.setStyleSheet("""
                                QComboBox {
                                    border: 2px solid black;
                                    border-radius: 10px;
                                    padding: 5px;
                                    background-color: lightblue;
                                    color: darkblue;
                                }
                                QComboBox QAbstractItemView {
                                    border: 1px solid gray;
                                    selection-background-color: lightgray;
                                    background: white;
                                }
                                """)
        # self.Selecao.show()

        self.imagemMaquina = QLabel(self.planoDeFundo)
        self.imagemMaquina.move(650, 50)  # Define a posição da imagem

        self.atualizarImagem(self.Selecao.currentText())

        #Definição do texto de seleção
        self.texto_label = QLabel("Selecione a máquina para receber dados", self.planoDeFundo)
        self.texto_label.move(50, 100)  
        self.texto_label.setFont(QFont("Arial", 14, QFont.Bold))  
        self.texto_label.setStyleSheet("color: white;")  
        self.texto_label.show()

        #Definição do botão utilizado
        self.botao = QPushButton("Inicializar Coleta de Dados", self.planoDeFundo)
        self.botao.move(50, 300)  
        self.botao.setFixedSize(200, 40)  
        self.botao.setParent(self.planoDeFundo)
        self.botao.setStyleSheet("""
                                QPushButton {
                                    background-color: darkgreen;
                                    color: white;
                                    border: 2px solid black;
                                    border-radius: 10px;
                                    font-size: 13px;
                                    font-weight: bold;
                                }
                                QPushButton:hover {
                                    background-color: lightgreen;
                                }
                                QPushButton:pressed {
                                    background-color: green;
                                    border: 4px solid white;
                                }
                                """)
        self.botao.clicked.connect(self.ComecarAquisicaoDados)  
        # self.botao.show()

    def atualizarImagem(self, event):
        texto = self.Selecao.currentText()
        if   texto == maquinas[0]:
            caminho_imagem = "Imagens/im.jpg"  
        elif texto == maquinas[1]:
            caminho_imagem = "Imagens/im2.png"
        elif texto == maquinas[2]:
            caminho_imagem = "Imagens/im3.png"
        else:
            caminho_imagem = "Imagens/im.jpg"

        pixmap = QPixmap(caminho_imagem)
        self.imagemMaquina.setPixmap(pixmap.scaled(300, 300))  # Ajusta o tamanho da imagem

    # def index_changed(self, i): # i is an int
    #     print("")

    def ComecarAquisicaoDados(self):
        escreverCSVTeste() 