##http://es.slideshare.net/ingenieriageologica1/capitulo-vi-procesamiento-digital-de-una-imagen
##http://python-para-impacientes.blogspot.com.co/2014/12/fundamentos-para-procesar-imagenes-con_16.html
##http://pybonacci.github.io/scipy-lecture-notes-ES/advanced/image_processing/index.html
import numpy as np ##C:\Python34\python -m pip install numpy
from PIL import Image
from copy import copy, deepcopy
import matplotlib.pyplot as plt

img = Image.open("Lenna.png").convert("RGB")
dados = Image.open("dados.png").convert("RGBA")

print(img.size, img.mode, img.format)

##L = R * 299/1000 + G * 587/1000 + B * 114/1000
img_gray = img.convert('L')

##img_gray.save("img_gray.jpg")

print(img_gray.size, img_gray.mode, img_gray.format)

##https://pillow.readthedocs.org/en/3.0.0/reference/Image.html#PIL.Image.Image.convert
##dtype es uint8 para imágenes de 8-bits (0-255)
a=np.asarray(img, dtype=np.uint8)
b=np.asarray(img_gray, dtype=np.uint8)

m_dado = np.asarray(dados, dtype=np.uint8)

print(m_dado[0])
c = deepcopy(a);

##for x in range(50, 200):
##    for y in range(50, 200):
##        c[x,y] = [0,0,0]
##
##with open("datos.txt","w") as file:
##    for fila in c:
##        for terna in fila:
##            file.write("({0},{1},{2});".format(int(terna[0]),int(terna[1]),int(terna[2])))
##        file.write("\n")
##
##Image.fromarray(c.astype(np.uint8)).save("prueba.jpg")

##plt.figure()
##plt.subplot(200)
plt.imshow(c)
##plt.subplot(122)
##plt.imshow(b)
plt.show()
