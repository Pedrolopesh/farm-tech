#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

// --- CONFIGURAÇÕES DE REDE ---
const char* ssid = "NOME_DO_SEU_WIFI";
const char* password = "SENHA_DO_SEU_WIFI";

// --- CONFIGURAÇÃO DA API ---
// Substitua pelo IP que você viu no ipconfig e a porta 8000
const char* serverName = "http://192.168.X.X:8000/interacoes"; 
const char* apiKey = "sua_chave_secreta_aqui"; // Deve ser igual à do main.py

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\n✅ Wi-Fi Conectado!");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverName);
    
    // Segurança e Integridade
    http.addHeader("Content-Type", "application/json");
    http.addHeader("X-API-KEY", apiKey);

    // Dados para análise de padrões e IA
    StaticJsonDocument<200> doc;
    doc["tempo_permanencia_seg"] = random(30, 300); 
    doc["toques_por_minuto"] = random(5, 120);
    doc["velocidade_toques"] = "media";

    String requestBody;
    serializeJson(doc, requestBody);

    int httpResponseCode = http.POST(requestBody);

    if (httpResponseCode > 0) {
      Serial.print("Dados enviados para a API! Status: ");
      Serial.println(httpResponseCode);
    } else {
      Serial.print("Erro no envio: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  }
  delay(15000); // Envia a cada 15 segundos
}