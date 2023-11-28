import matplotlib.pyplot as plt
from skimage import io
imagem = io.imread('picos.jpg')
imagem.shape

plt.figure(figsize=(15,30))
plt.imshow(imagem);

red = imagem[:,:,0]
green = imagem[:,:,1]
blue = imagem[:,:,2]
print('Vermelho:', red)
print('Verde:', green)
print('Blue:', blue)

blue.shape

#