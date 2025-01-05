from imports import *

def sen(x): return np.sin(x)

# Função que simula um processo demorado
def escreverCSVTeste(nomeArquivoCSV='Dados/dados.csv'):
    contador = 0
    dados = [0,0]
    print("ok")

    with open(nomeArquivoCSV, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Eixo_X', 'Eixo_Y']) 

    while contador < 400:
        print(contador)
        dados[0] += 0.1  
        dados[1] = sen(dados[0])
       
        with open(nomeArquivoCSV, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([round(dados[0],3), round(dados[1],3)])
            file.flush()  

        t.sleep(0.1)

        contador += 1

if __name__ == "__main__":
    escreverCSVTeste()
