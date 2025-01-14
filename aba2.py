from imports import *
from classesAux import *
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QFileDialog


class aba2(QWidget):
    def __init__(self, imagemFundo):
        super().__init__()

        # Define o plano de fundo
        self.imagemFundo = imagemFundo
        self.planoDeFundo = definirPlanoDeFundo(self.imagemFundo)
        self.planoDeFundo.setGeometry(0, 0, self.width(), self.height())

        # Criação de um layout pai para todos os widgets
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.planoDeFundo)

        # Definição do texto explicação
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
        self.botao_grafico = QPushButton("Selecionar e Mostrar Gráfico", self.planoDeFundo)
        self.botao_grafico.move(50, 300)
        self.botao_grafico.setFixedSize(200, 50)
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
        self.botao_grafico.clicked.connect(self.selecionar_e_mostrar_grafico)

    def selecionar_e_mostrar_grafico(self):
        # Abrir o diálogo para selecionar arquivos CSV
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Selecione um Arquivo CSV", "", "CSV Files (*.csv);;All Files (*)", options=options
        )

        if file_path:
            try:
                # Ler o arquivo CSV
                data = pd.read_csv(file_path)
                if data.shape[1] < 2:
                    self.texto_label.setText("O arquivo precisa ter pelo menos 2 colunas.")
                    return

                # Obter os textos do gráfico
                titulo = self.tituloGrafico.text() or "Gráfico dos Dados"
                xlabel = self.tituloXlabel.text() or "X"
                ylabel = self.tituloYlabel.text() or "Y"

                # Plotar os dados
                plt.figure(figsize=(8, 6))
                plt.plot(data.iloc[:, 2], data.iloc[:, 0], label="Y vs X")
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                plt.title(titulo)
                plt.legend()
                plt.grid()
                plt.show()

                self.texto_label.setText("Gráfico plotado com sucesso!")
            except Exception as e:
                self.texto_label.setText(f"Erro ao processar o arquivo: {str(e)}")
