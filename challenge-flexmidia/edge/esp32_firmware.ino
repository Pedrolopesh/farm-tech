/*
 * EDUBOT - Firmware ESP32 (Prova de Conceito / PoC)
 * Este código demonstra a integração da camada de Edge Computing (IoT)
 * com a nossa API FastAPI, respeitando os requisitos de Cognitive CyberSecurity.
 */

#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

// --- CONFIGURAÇÕES DE REDE ---
const char* ssid = "WIFI_DA_FACULDADE";
const char* password = "SENHA_DO_WIFI";

// --- CONFIGURAÇÃO DA API ---
// Exemplo de endpoint apontando para o servidor local ou nuvem onde a API está hospedada
const char* serverName = "http://SEU_IP_LOCAL:8000/api/sensores/interacao";
const char* apiKey = "sua_chave_secreta_aqui"; // Autenticação obrigatória

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\n✅ Wi-Fi Conectado! Iniciando monitoramento do Totem...");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverName);

    // Cabeçalhos de Segurança (Cognitive CyberSecurity)
    http.addHeader("Content-Type", "application/json");
    http.addHeader("X-API-KEY", apiKey);

    // Montagem do Payload (Exatamente como o Pydantic da API exige)
    StaticJsonDocument<256> doc;
    doc["session_id"] = "ESP32-" + String(millis());
    doc["timestamp"] = "2026-03-06 20:00:00"; 
    doc["status_ativacao"] = 1;
    doc["tipo_interacao"] = "média"; 
    doc["tempo_permanencia_seg"] = random(30, 300);
    doc["toques_por_minuto"] = random(5, 120);
    doc["velocidade_toques"] = "media";

    String requestBody;
    serializeJson(doc, requestBody);
    
    // Disparo dos dados via POST
    int httpResponseCode = http.POST(requestBody);
    
    if (httpResponseCode > 0) {
      Serial.print("✅ Dados enviados para a API! Status: ");
      Serial.println(httpResponseCode);
    } else {
      Serial.print("❌ Erro no envio: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  }
  delay(15000); // Aguarda 15 segundos até a próxima leitura do sensor
}
