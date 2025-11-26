##########################################################
# Visualização de Dados Espaciais
##########################################################

install.packages(c("geostan", "ggplot2", "gridExtra"))
library(geostan)
library(ggplot2)
library(gridExtra)
data("georgia")

# Utilizamos a função sp_diag() para visualizar a distribuição espacial
# da porcentagem de adultos com diploma universitário
# em cada condado do estado da Geórgia, nos Estados Unidos.
sp_diag(georgia$college, georgia, name  = "College (%)")

# Cria uma matriz de pesos espaciais no estilo binário,
# a partir do objeto georgia.
# Essa matriz será usada para avaliar
# a autocorrelação espacial da variável de porcentagem de diplomas
W <- shape2mat(georgia)

# Gera um gráfico de dispersão para o Diagrama de Moran,
# utilizando a variável de porcentagem de faculdades
# e a matriz de pesos espaciais W para avaliar a autocorrelação espacial.

# a inclinação da reta ajustada sugere:
# - positiva: valores próximos tendem a se agrupar
# - 0 (neutra): não há correlação espacial
# - negativa: valores próximos tendem a estar dispersos
moran_plot(georgia$college, W)
