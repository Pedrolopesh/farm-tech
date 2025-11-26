library(geostan)
library(ggplot2)
library(gridExtra)
data("georgia")

# A função sp_diag() é usada para visualizar a distribuição espacial de uma variável 
# (neste caso, a porcentagem de faculdades) em um mapa geográfico (representado pelo objeto georgia). 
# Permite a análise de padrões espaciais e a identificação de agrupamentos ou dispersões dessa variável 
# na área geográfica estudada.
sp_diag(georgia$college, georgia, name = "College (%)")

# Cria uma matriz de pesos espaciais no estilo binário a partir do objeto georgia. 
# Essa matriz será usada para avaliar a autocorrelação espacial da variável de porcentagem de faculdades.
W <- shape2mat(georgia, style = "W")

# Gera um gráfico de dispersão para o Diagrama de Moran, utilizando a variável de porcentagem de faculdades 
# e a matriz de pesos espaciais W para avaliar a autocorrelação espacial.
moran_plot(georgia$college, W)

# Calcula o índice de autocorrelação espacial de Moran para a variável de porcentagem de faculdades, 
# utilizando a matriz de pesos espaciais W.
mc(georgia$college, W)

# Cria outra matriz de pesos espaciais no estilo binário a partir do objeto georgia. 
# Essa matriz será usada para avaliar a autocorrelação espacial da variável de porcentagem de faculdades.
A <- shape2mat(georgia, "B")

# Gera outro gráfico de dispersão para o Diagrama de Moran, utilizando a mesma variável e uma matriz de 
# pesos espaciais diferente (A) para avaliar a autocorrelação espacial.
moran_plot(georgia$college, A)a