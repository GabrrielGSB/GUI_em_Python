from imports import *
from classesAux import *

class aba2(QWidget):
    def __init__(self, imagemFundo):
        super().__init__()
        self.imagemFundo = imagemFundo

        # Define o plano de fundo
        self.planoDeFundo = definirPlanoDeFundo(self.imagemFundo)
        self.planoDeFundo.setGeometry(0, 0, self.width(), self.height())

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.planoDeFundo)

        # Botão para abrir o gráfico em uma nova janela
        self.botao_grafico = QPushButton("Mostrar Gráfico", self.planoDeFundo)
        self.botao_grafico.move(50, 500)
        self.botao_grafico.setFixedSize(150, 50)
        self.botao_grafico.setStyleSheet("""
            QPushButton {
                background-color: blue;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: lightblue;
            }
        """)
        self.botao_grafico.clicked.connect(self.mostrarGrafico)

        # Caixas de textos para alterar os textos do gráfico
        self.tituloGrafico = QLineEdit(self.planoDeFundo)
        self.tituloGrafico.setPlaceholderText("Digite o título do gráfico")
        self.tituloGrafico.move(50, 120)
        self.tituloGrafico.setFixedSize(300, 40)
        self.tituloGrafico.setStyleSheet("""
            QLineEdit {
                border: 2px solid gray;
                border-radius: 10px;
                padding: 5px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border-color: blue;
            }
        """)

        self.tituloXlabel = QLineEdit(self.planoDeFundo)
        self.tituloXlabel.setPlaceholderText("Digite o nome do eixo X")
        self.tituloXlabel.move(50, 200)
        self.tituloXlabel.setFixedSize(300, 40)
        self.tituloXlabel.setStyleSheet("""
                                            QLineEdit {
                                                border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 5px;
                                                font-size: 14px;
                                            }
                                            QLineEdit:focus {
                                                border-color: blue;
                                            }
                                        """)        
        
        self.tituloYlabel = QLineEdit(self.planoDeFundo)
        self.tituloYlabel.setPlaceholderText("Digite o nome do eixo Y")
        self.tituloYlabel.move(50, 300)
        self.tituloYlabel.setFixedSize(300, 40)
        self.tituloYlabel.setStyleSheet("""
                                            QLineEdit {
                                                border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 5px;
                                                font-size: 14px;
                                            }
                                            QLineEdit:focus {
                                                border-color: blue;
                                            }
                                        """)

        self.janelaGrafico = None
        
    def mostrarGrafico(self):
        #Abre uma nova janela com o gráfico gerado pelo matplotlib.
        if not self.janelaGrafico:
            self.janelaGrafico = JanelaGrafico()

        novoTitulo = self.tituloGrafico.text()
        novaXlabel = self.tituloXlabel.text()
        novaYlabel = self.tituloYlabel.text()

        if novoTitulo or novaXlabel or novaYlabel:
            self.janelaGrafico.grafico.atualizarTitulo(novoTitulo)
            self.janelaGrafico.grafico.atualizarXlabel(novaXlabel)
            self.janelaGrafico.grafico.atualizarYlabel(novaYlabel)

        self.janelaGrafico.grafico.iniciarAtualizacao()
        self.janelaGrafico.show()