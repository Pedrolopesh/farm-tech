
# estatisticas.R — Estatísticas básicas do CSV (Soja & Açaí, 2010–2024)
dados <- read.csv("data/dados_agricolas_soja_acai_2010_2024.csv", sep = ",", header = TRUE, stringsAsFactors = FALSE)

to_num <- function(x) suppressWarnings(as.numeric(x))
numcols <- c("area_ha","producao_t","produtividade_t_ha")
for (c in numcols) { dados[[c]] <- to_num(dados[[c]]) }

cat("=== Estatísticas básicas (gerais) ===\n")
print(summary(dados[numcols]))

cat("\n=== Médias por cultura ===\n")
print(aggregate(dados[numcols], by = list(cultura = dados$cultura), FUN = function(x) mean(x, na.rm = TRUE)))
