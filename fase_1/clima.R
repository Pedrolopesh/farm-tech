# Instalar pacotes caso não tenha
# install.packages(c("httr", "jsonlite"))

library(httr)
library(jsonlite)

# Definir coordenadas (Mato Grosso, Cuiaba, Brasil por exemplo)
latitude <- -15.6010
longitude <- -56.0974

# Endpoint da API Open-Meteo (sem necessidade de chave)
url <- paste0(
  "https://api.open-meteo.com/v1/forecast?",
  "latitude=", latitude,
  "&longitude=", longitude,
  "&current_weather=true"
)

# Requisição HTTP GET
res <- GET(url)

# Verificar status da resposta
if (status_code(res) == 200) {
  # Converter JSON para lista em R
  dados <- fromJSON(content(res, "text"))
  
  # Extrair informações do tempo atual
  clima <- dados$current_weather
  cat("📍 Localização aproximada (lat:", latitude, 
      "lon:", longitude, ")\n")
  cat("🌡️ Temperatura:", clima$temperature, "°C\n")
  cat("💨 Vento:", clima$windspeed, "km/h\n")
  cat("🧭 Direção do vento:", clima$winddirection, "°\n")
  cat("⏰ Última atualização:", clima$time, "\n")
  
} else {
  cat("Erro ao acessar API. Código HTTP:", status_code(res), "\n")
}
