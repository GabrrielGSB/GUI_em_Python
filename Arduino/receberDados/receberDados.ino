#include "WiFi.h"

const char *ssid     = "ESP32_Server";
const char *password = "123456789";
const char *host     = "192.168.4.1"; 
const uint8_t port   =  80;

struct sensorData { float AngleRoll,AnglePitch,kalmanAngleRoll,kalmanAnglePitch; };

WiFiClient client;

void setup() 
{
  Serial.begin(115200);
  conectarServidor();
}

void loop() 
{
  receberDados(100);
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

void receberDados(uint16_t intervalo)
{
  if (client.connect(host, port)) 
  { 
    // Esperar receber os dados
    while (client.available() < sizeof(sensorData)){}
    
    // Ler dados binários
    sensorData dadosRecebidos;
    client.read((uint8_t*)&dadosRecebidos, sizeof(dadosRecebidos));
    Serial.printf(dadosRecebidos.kalmanAngleRoll);
    // Exibir os dados recebidos
    // Serial.printf("AngleRoll: %f, AnglePitch: %f, kalmanAngleRoll: %f, kalmanAnglePitch: %f, Tempo: %d \n",
    //               dadosRecebidos.AngleRoll,
    //               dadosRecebidos.AnglePitch,
    //               dadosRecebidos.kalmanAngleRoll,
    //               dadosRecebidos.kalmanAngleRoll,
    //               millis());
    
    // delay(intervalo); // Aguarde antes de tentar novamente
  }
  else
  { 
    Serial.println("Falha na conexão com o servidor");
    delay(100);
  }  
}
