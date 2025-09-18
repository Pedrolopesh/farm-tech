# Carregar pacotes
library(readr)
library(dplyr)

# Ler arquivo CSV
df <- read_csv("applications.csv")

# Selecionar apenas colunas numéricas relevantes
numericos <- df %>% 
  select(cultura, taxa_ml_por_m, num_ruas, comprimento_m, total_metros, total_ml, litros_totais)

# Calcular estatísticas por cultura (Soja / Açaí)
estatisticas <- numericos %>%
  group_by(cultura) %>%
  summarise(
    across(
      where(is.numeric),
      list(
        media = mean,
        desvio = sd,
        minimo = min,
        maximo = max
      ),
      na.rm = TRUE
    )
  )

print(estatisticas)
