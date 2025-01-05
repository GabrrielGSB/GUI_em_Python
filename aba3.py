from imports import *
from classesAux import *

class aba3(QWidget):
    def __init__(self, imagemFundo, nomeArquivoCSV):
        super().__init__()

        # Definição do plano de fundo 
        self.imagemFundo = imagemFundo
        self.planoDeFundo = definirPlanoDeFundo(self.imagemFundo)
        self.planoDeFundo.setGeometry(0, 0, self.width(), self.height())

        # Criação de um layout pai para todos os widgets
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0) 
        self.layout.addWidget(self.planoDeFundo)

        # Criação do botão
        self.botao = QPushButton("Executar Script Python", self)
        self.botao.clicked.connect(self.executar_script)

        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Exemplo de Execução Paralela")

    def executar_script(self):
        # Criação de um processo para rodar o arquivo .py em paralelo
        self.processo = QProcess(self)
        
        # Certifique-se de que o caminho do script está correto
        script_path = "script.py"  # Ajuste o caminho conforme necessário
        self.processo.start("python3", [script_path])

        # Conectar sinais para captura de saída
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

# # Executa a aplicação PyQt
# if __name__ == '__main__':
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec_()
