from imports import *

def sen(x): return np.sin(x)

def escreverCSV(csv_file):
    ser = serial.Serial('/dev/ttyUSB1', 115200) 

    try:
        while ser.is_open:
            line = ser.readline().decode('utf-8').split(',')
            print(line)

            try:
                # Extração de valores
                angleRoll    = line[0].split(':')[1].strip()
                anglePitch   = line[1].split(':')[1].strip()
                kalmanRoll   = line[2].split(':')[1].strip()
                kalmanPitch  = line[3].split(':')[1].strip()
                deslocamento = line[4].split(':')[1].strip()
                tempo        = line[5].split(':')[1].strip()

                # Escreve os dados no CSV
                with open(csv_file, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([angleRoll, anglePitch, kalmanRoll, kalmanPitch, deslocamento, tempo])
                    file.flush()  

            except Exception as e:
                print("Erro ao processar linha:", e)

    except KeyboardInterrupt:
        print("Finalizando...")
    finally:
        ser.close()


if __name__ == "__main__":
    
    dadosTempo = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
    nomeArquivoCSV = f"Dados/dados_{dadosTempo}.csv"
    # nomeArquivoCSV = 'Dados/dados.csv'

    # Cria o novo arquivo e escreve o cabeçalho
    with open(nomeArquivoCSV, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['AngleRoll', 'AnglePitch', 'KalmanAngleRoll', 'KalmanAnglePitch', 'Deslocamento', 'Tempo'])

    escreverCSV(nomeArquivoCSV)
