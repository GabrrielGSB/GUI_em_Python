from imports import *
from classesAux import *

class aba2(QWidget):
    def __init__(self, imagemFundo):
        super().__init__()

        # Define o plano de fundo
        self.imagemFundo = imagemFundo
        self.planoDeFundo = definirPlanoDeFundo(self.imagemFundo)
        self.planoDeFundo.setGeometry(0, 0, self.width(), self.height())

        #Criação de um layout pai para todos os widgets
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.planoDeFundo)

        #Definição do texto explicação
        self.texto_label = QLabel("Nomeie o gráficos e seus eixos", self.planoDeFundo)
        self.texto_label.move(50, 80)  
        self.texto_label.setFont(QFont("Arial", 14, QFont.Bold))  
        self.texto_label.setStyleSheet("color: white;")  
        self.texto_label.show()

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
        self.tituloXlabel.move(50, 170)
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
        self.tituloYlabel.move(50, 220)
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
 
        # Botão para abrir o gráfico em uma nova janela
        self.botao_grafico = QPushButton("Mostrar Gráfico", self.planoDeFundo)
        self.botao_grafico.move(50, 300)
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
        # self.botao_grafico.clicked.connect(self.executarScript)

    def mostrarGrafico(self):
        self.janelaGrafico = None
        
        if not self.janelaGrafico:
            self.janelaGrafico = JanelaGrafico()

        novoTitulo = self.tituloGrafico.text()
        novaXlabel = self.tituloXlabel.text()
        novaYlabel = self.tituloYlabel.text()

        if novoTitulo: self.janelaGrafico.grafico.atualizarTitulo(novoTitulo)
        if novaXlabel: self.janelaGrafico.grafico.atualizarXlabel(novaXlabel)
        if novaYlabel: self.janelaGrafico.grafico.atualizarYlabel(novaYlabel)

        self.janelaGrafico.grafico.iniciarAtualizacao()
        self.janelaGrafico.show()
        self.janelaGrafico.grafico.atualizarGrafico()

    