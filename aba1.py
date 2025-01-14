from imports import *
from classesAux import *

maquinas = ["maquina1", "maquina2", "maquina3"]

class aba1(QWidget):
    def __init__(self, imagemFundo):
        super().__init__()

        #Definição do plano de fundo 
        self.imagemFundo = imagemFundo
        self.planoDeFundo = definirPlanoDeFundo(self.imagemFundo)
        self.planoDeFundo.setGeometry(0, 0, self.width(), self.height())

        #Criação de um layout pai para todos os widgets
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0) 
        self.layout.addWidget(self.planoDeFundo)

        #Definição do texto de seleção
        self.texto_label = QLabel("Selecione a máquina para receber dados", self.planoDeFundo)
        self.texto_label.move(50, 25)  
        self.texto_label.setFont(QFont("Arial", 14, QFont.Bold))  
        self.texto_label.setStyleSheet("color: white;")  
        self.texto_label.show()

        #Definição da caixa de seleção de imagem e aquisição de dados
        self.Selecao = QComboBox()
        self.Selecao.move(50,50)
        self.Selecao.setFixedSize(380, 30)
        self.Selecao.addItems([maquinas[0], maquinas[1], maquinas[2]])
        self.Selecao.currentTextChanged.connect(self.mostrarImagemComboBox)
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

        #Definição da imagem atralada a ComboBox
        self.imagemMaquina = QLabel(self.planoDeFundo)
        self.imagemMaquina.move(650, 50) 

        #Chamamento da função para mostrar a imagemMaquina a primeira vez 
        self.mostrarImagemComboBox(self.Selecao.currentText())
       
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
        self.botao.clicked.connect(self.executarScript)
        self.botao.clicked.connect(self.mostrarGrafico)
        
    #Definição das funções usadas
    def mostrarImagemComboBox(self, event):
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
        self.imagemMaquina.setPixmap(pixmap.scaled(300, 300)) 

    def mostrarGrafico(self):
            self.janelaGrafico = None
            
            if not self.janelaGrafico:
                self.janelaGrafico = JanelaGrafico()

            novoTitulo = "Dados em Tempo Real"
            novaXlabel = "número do dado"
            novaYlabel = "valor do dado"

            if novoTitulo: self.janelaGrafico.grafico.atualizarTitulo(novoTitulo)
            if novaXlabel: self.janelaGrafico.grafico.atualizarXlabel(novaXlabel)
            if novaYlabel: self.janelaGrafico.grafico.atualizarYlabel(novaYlabel)

            t.sleep(2.5)
            self.janelaGrafico.grafico.iniciarAtualizacao()
            self.janelaGrafico.show()
            self.janelaGrafico.grafico.atualizarGrafico()


    def executarScript(self):
        self.processo = QProcess(self)

        script_path = "iniciarColetaDados.py"  
  

        self.processo.start("python3", [script_path])

        self.processo.readyReadStandardOutput.connect(self.ler_saida)
        self.processo.readyReadStandardError.connect(self.ler_erro)
        self.processo.finished.connect(self.processo_terminou)

    def ler_saida(self):
        # Captura a saída padrão do script Python
        saida = self.processo.readAllStandardOutput().data().decode()
        print("Saída do Script:", saida)  # Ou exiba na GUI

    def ler_erro(self):
        # Captura a saída de erro do script Python
        erro = self.processo.readAllStandardError().data().decode()
        print("Erro no Script:", erro)  # Ou exiba na GUI

    def processo_terminou(self):
        print("O script Python terminou sua execução.")
   