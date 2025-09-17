# Carregar pacotes
library(dplyr)
library(openxlsx)
# Ler o CSV
df <- read.csv("dados_agricolas_soja_acai_2010_2024.csv")

# Selecionar apenas as colunas relevantes
df <- df %>% select(ano, cultura, area_ha, producao_t, produtividade_t_ha)

# Calcular estatísticas descritivas por cultura
estatisticas <- df %>%
  group_by(cultura) %>%
  summarise(
    area_media = mean(area_ha, na.rm = TRUE),
    area_mediana = median(area_ha, na.rm = TRUE),
    area_dp = sd(area_ha, na.rm = TRUE),
    area_min = min(area_ha, na.rm = TRUE),
    area_max = max(area_ha, na.rm = TRUE),
    
    producao_media = mean(producao_t, na.rm = TRUE),
    producao_mediana = median(producao_t, na.rm = TRUE),
    producao_dp = sd(producao_t, na.rm = TRUE),
    producao_min = min(producao_t, na.rm = TRUE),
    producao_max = max(producao_t, na.rm = TRUE),
    
    produtividade_media = mean(produtividade_t_ha, na.rm = TRUE),
    produtividade_mediana = median(produtividade_t_ha, na.rm = TRUE),
    produtividade_dp = sd(produtividade_t_ha, na.rm = TRUE),
    produtividade_min = min(produtividade_t_ha, na.rm = TRUE),
    produtividade_max = max(produtividade_t_ha, na.rm = TRUE)
  )

# Exibir resultados
print(estatisticas)

# Criar arquivo Excel
write.xlsx(estatisticas, file = "estatisticas_agricolas.xlsx", sheetName = "Resumo", rowNames = FALSE)