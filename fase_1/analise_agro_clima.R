
# analise_agro_clima.R — Estatísticas (Soja & Açaí) + Clima (OpenWeather)
suppressWarnings(suppressMessages({ library(httr); library(jsonlite) }))

# ===== Estatísticas do CSV =====
dados <- read.csv("data/dados_agricolas_soja_acai_2010_2024.csv", sep = ",", header = TRUE, stringsAsFactors = FALSE)
to_num <- function(x) suppressWarnings(as.numeric(x))
numcols <- c("area_ha","producao_t","produtividade_t_ha")
for (c in numcols) { dados[[c]] <- to_num(dados[[c]]) }

cat("=== Estatísticas Básicas — Soja & Açaí (2010–2024) ===\n")
print(summary(dados[numcols]))

cat("\n=== Médias por Cultura ===\n")
print(aggregate(dados[numcols], by = list(cultura = dados$cultura), FUN = function(x) mean(x, na.rm = TRUE)))

# ===== Clima (OpenWeather) =====
api_key <- "41d110b78a647279cf968bb33918ec64"  # chave de apresentação
cidade <- "Belem,BR"  # exemplo de região produtora de açaí
url <- sprintf("https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric&lang=pt_br", cidade, api_key)
res <- GET(url)

cat("\n=== Clima Atual ===\n")
if (status_code(res) == 200) {
  clima <- fromJSON(content(res, "text", encoding="UTF-8"))
  cat("Cidade:", cidade, "\n")
  cat("Temperatura:", clima$main$temp, "°C\n")
  cat("Umidade:", clima$main$humidity, "%\n")
  cat("Condição:", clima$weather[[1]]$description, "\n")
} else {
  cat("Erro ao consultar API. Código:", status_code(res), "\n")
}

cat("\nNota: CSV usado = dados_agricolas_soja_acai_2010_2024.csv. Cultura: Soja & Açaí. Cidade climática de exemplo: Belém-PA.\n")
