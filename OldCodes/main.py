from mainImports import *
from CriarCSV import *

if __name__ == "__main__":
    # Gerar um nome de arquivo único com base na data e hora
    dadosTempo = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
    nomeArquivoCSV = f"dados_{dadosTempo}.csv"

    # Cria o novo arquivo e escreve o cabeçalho
    with open(nomeArquivoCSV, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Pontos_no_Eixo_X', 'Pontos_no_Eixo_Y'])

    # Cria os processos e inicializa eles
    nucleo1 = multiprocessing.Process(target=escreverCSVTeste,     args=(nomeArquivoCSV,))
    nucleo2 = multiprocessing.Process(target=criarGraficoDinamico, args=(nomeArquivoCSV,))

    nucleo1.start()
    nucleo2.start()
    
    nucleo1.join()
    nucleo2.join()