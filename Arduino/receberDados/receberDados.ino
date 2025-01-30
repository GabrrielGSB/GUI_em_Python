#include "WiFi.h"

const char *ssid     = "ESP32_Server";
const char *password = "123456789";
const char *host     = "192.168.4.1"; 
const uint8_t port   =  80;

struct sensorData { float AngleRoll,AnglePitch,kalmanAngleRoll,kalmanAnglePitch,deslocamento; };

WiFiClient client;

void setup() 
{
  Serial.begin(115200);
  conectarServidor();
}

void loop() 
{
  receberDados();
}

void conectarServidor()
{
  // Conectar ao Wi-Fi do servidor
  WiFi.begin(ssid, password);
  Serial.println("Conectando ao Wi-Fi...");
  while (WiFi.status() != WL_CONNECTED) 
  {
      delay(1000);
      Serial.print(".");
  }
  Serial.println("Conectado ao Wi-Fi");
}

void receberDados()
{
  if (client.connect(host, port)) 
  { 
    // Esperar receber os dados
    while (client.available() < sizeof(sensorData)){}
    
    // Ler dados binários
    sensorData dadosRecebidos;
    client.read((uint8_t*)&dadosRecebidos, sizeof(dadosRecebidos));
 
    // Exibir os dados recebidos
    Serial.printf("AngleRoll: %f, AnglePitch: %f, kalmanAngleRoll: %f, kalmanAnglePitch: %f, deslocamento: %f, Tempo: %d \n",
                   dadosRecebidos.AngleRoll,
                   dadosRecebidos.AnglePitch,
                   dadosRecebidos.kalmanAngleRoll,
                   dadosRecebidos.kalmanAnglePitch,
                   dadosRecebidos.deslocamento,
                   millis());
  }
  else
  { 
    Serial.println("Falha na conexão com o servidor");
    delay(100);
  }  
}
