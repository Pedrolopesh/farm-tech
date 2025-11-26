# Carregar bibliotecas necessárias
library(sp)
library(spdep)

# Carregar conjunto de dados meuse
data(meuse)

# Converter o conjunto de dados meuse para um objeto SpatialPointsDataFrame
coordinates(meuse) <- c("x", "y")

# Calcular os vizinhos mais próximos usando a distância de Euclides
knn <- knearneigh(coordinates(meuse), k = 6)

# Converter os vizinhos mais próximos em uma matriz de pesos espaciais
listw <- knn2nb(knn)

# Tornar a matriz de pesos espaciais em uma matriz binária de pesos espaciais
listw <- nb2listw(listw, style = "B")

# Medidas de Centralidade
# Calcular a média espacial
media_espacial <- mean(meuse$zinc, na.rm = TRUE)
print(media_espacial)

# Calcular a mediana espacial
mediana_espacial <- median(meuse$zinc)
print(mediana_espacial)

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
# Calcular o Índice de Moran
indice_moran <- moran.test(meuse$zinc, listw)
print(indice_moran)

# Calcular o Índice de Geary
indice_geary <- geary.test(meuse$zinc, listw)
print(indice_geary)

# Calcular o Índice de LISA
indice_lisa <- localmoran(meuse$zinc, listw)
print(indice_lisa)