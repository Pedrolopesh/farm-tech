##############################################################
#                 Estatística Espacial Descritiva            #
##############################################################

# Carregar bibliotecas necessárias
library(sp)        # inclui o conjunto de dados meuse
library(spdep)     # biblioteca com funções para análise espacial
library(DescTools) # coletânea de funções estatísticas

# "meuse" é um conjunto de dados que contém informações sobre
# a qualidade da água e a concentração de metais pesados em solos
# e sedimentos do rio Meuse, na Holanda.

# Carregar conjunto de dados meuse
data(meuse)

# Medidas de Centralidade

# Calculando a média espacial da concentração de zinco
media_espacial <- mean(meuse$zinc, na.rm = TRUE)
print(media_espacial)

# Calcular a mediana espacial da concentração de zinco
mediana_espacial <- median(meuse$zinc)
print(mediana_espacial)

# Calcular a moda espacial da concentração de zinco
moda_espacial <- Mode(meuse$zinc)
print(moda_espacial)

# Medidas de Dispersão
# Calcular o desvio padrão espacial e a variância espacial
desvio_padrao_espacial <- sd(meuse$zinc)
print(desvio_padrao_espacial)

variancia_espacial <- var(meuse$zinc)
print(variancia_espacial)

# Calcular o coeficiente de variação espacial
coeficiente_variacao_espacial <- desvio_padrao_espacial / media_espacial
print(coeficiente_variacao_espacial)

# Índices de Autocorrelação Espacial
# Converter o conjunto de dados meuse para um objeto SpatialPointsDataFrame
coordinates(meuse) <- c("x", "y")

# Calcular os vizinhos mais próximos usando a distância de Euclides
knn <- knearneigh(coordinates(meuse), k = 6)

# Converter os vizinhos mais próximos em uma matriz de pesos espaciais
listw <- knn2nb(knn)

# Tornar a matriz de pesos espaciais
# em uma matriz binária de pesos espaciais
listw <- nb2listw(listw, style = "B")

# Tornar a matriz de pesos espaciais
# em uma matriz binária de pesos espaciais
listw <- nb2listw(listw, style = "B")

# Calcular o Índice de Moran
# Teste de hipóteses estatístico,
# em que H0 indica a ausência de correlação espacial, logo,
# se p-value < 0.05, podemos assumir que há correlação espacial
indice_moran <- moran.test(meuse$zinc, listw)
print(indice_moran)



# Calcular o Índice de Geary:
# - menor que 1: indica autocorrelação positiva, ou seja,
#                valores semelhantes tendem a estar próximos
# - próximo a 1: indica ausência de autocorrelação espacial
# - maior que 1: indica autocorrelação negativa, ou seja,
#                valores semelhantes tendem a estar distantes
#
indice_geary <- geary.test(meuse$zinc, listw) 
print(indice_geary)

