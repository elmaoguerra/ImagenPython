##http://es.slideshare.net/ingenieriageologica1/capitulo-vi-procesamiento-digital-de-una-imagen
##http://python-para-impacientes.blogspot.com.co/2014/12/fundamentos-para-procesar-imagenes-con_16.html
##http://pybonacci.github.io/scipy-lecture-notes-ES/advanced/image_processing/index.html
import numpy as np ##C:\Python34\python -m pip install numpy
from PIL import Image
from copy import copy, deepcopy
import matplotlib.pyplot as plt

img = Image.open("Lenna.jpg")
dados = Image.open("dados.png")

print(img.size, img.mode, img.format)
print(dados.size, dados.mode, dados.format)

a = np.asarray(img, dtype="uint8")
b = np.asarray(dados, dtype=np.uint8)

print("\n{0} elementos.\n".format(len(b)))
## Que es un pixel?

print("Info del pixel: "+ str(b[100][200]))

## Convertir una imagen a escala de grises
## Poroporcion de L = R * 299/1000 + G * 587/1000 + B * 114/1000
##img_gray = img.convert('L')

c = deepcopy(a)
d=[]
for x in range(0, len(c)):
    aux = []
    for y in range(0, len(c[x])):
        var = c[x,y][0]*(299/1000) + c[x,y][1]*(587/1000) + c[x,y][2]*(114/1000)
        aux.append(int(var))
    d.append(aux)
        
x = np.array(d, dtype=np.uint8)
Image.fromarray(x.astype(np.uint8)).save("LennaGris.jpg")

##https://pillow.readthedocs.org/en/3.0.0/reference/Image.html#PIL.Image.Image.convert
##dtype es uint8 para imágenes de 8-bits (0-255)

gray = Image.open("LennaGris.jpg")
print(gray.size, gray.mode, gray.format)

m_dado = np.asarray(dados, dtype=np.uint32)

for x in range(50, 200):
    for y in range(50, 200):
        c[x,y] = [0,0,0]

with open("datos.txt","w") as file:
    for fila in c:
        for terna in fila:
            file.write("({0},{1},{2});".format(int(terna[0]),int(terna[1]),int(terna[2])))
        file.write("\n")

Image.fromarray(c.astype(np.uint8)).save("prueba.jpg")

####plt.figure()
####plt.subplot(200)
##plt.imshow(a)
####plt.subplot(122)
####plt.imshow(b)
##plt.show()
