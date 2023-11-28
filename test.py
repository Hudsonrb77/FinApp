from skimage import io

# Carregue a imagem colorida
imagem = io.imread('picos.jpg')

canalVermelho = imagem[:, :, 0]
canalVerde = imagem[:, :, 1]
canalAzul = imagem[:, :, 2]

maiorVermelho = menorVermelho = canalVermelho[0, 0]
maiorVerde = menorVerde = canalVerde[0, 0]
maiorAzul = menorAzul = canalAzul[0, 0]


for linha in range(imagem.shape[0]):
    for coluna in range(imagem.shape[1]):
        vermelho = canalVermelho[linha, coluna]
        verde = canalVerde[linha, coluna]
        azul = canalAzul[linha, coluna]

        if vermelho > maiorVermelho:
            maiorVermelho = vermelho
        if vermelho < menorVermelho:
            menorVermelho = vermelho

        if verde > maiorVerde:
            maiorVerde = verde
        if verde < menorVerde:
            menorVerde = verde

        if azul > maiorAzul:
            maiorAzul = azul
        if azul < menorAzul:
            menorAzul = azul

# Exiba os resultados
print("Componente Vermelha:")
print("Maior intensidade: {}".format(maiorVermelho))
print("Menor intensidade: {}".format(menorVermelho))

print("Componente Verde:")
print("Maior intensidade: {}".format(maiorVerde))
print("Menor intensidade: {}".format(menorVerde))

print("Componente Azul:")
print("Maior intensidade: {}".format(maiorAzul))
print("Menor intensidade: {}".format(menorAzul))