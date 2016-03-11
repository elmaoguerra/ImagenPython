##http://es.slideshare.net/ingenieriageologica1/capitulo-vi-procesamiento-digital-de-una-imagen
##http://python-para-impacientes.blogspot.com.co/2014/12/fundamentos-para-procesar-imagenes-con_16.html
##http://pybonacci.github.io/scipy-lecture-notes-ES/advanced/image_processing/index.html

import numpy as np ##C:\Python34\python -m pip install numpy
from PIL import Image
import matplotlib.pyplot as plt
from copy import copy, deepcopy


img = Image.open("Lenna.jpg")
dados = Image.open("dados.png")

print(img.size, img.mode, img.format)
print(dados.size, dados.mode, dados.format)

a = np.asarray(img, dtype=np.uint8)
b = np.asarray(dados, dtype=np.uint8)

print("\n{0} elementos.\n".format(len(b)))

print("Info del pixel: "+ str(b[100][200]))

## Que es un pixel?
## Convertir una imagen a escala de grises
## Poroporcion de L = R * 299/1000 + G * 587/1000 + B * 114/1000
##img_gray = img.convert('L')
##https://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale

##outputRed = (inputRed * .393) + (inputGreen *.769) + (inputBlue * .189)

##outputGreen = (inputRed * .349) + (inputGreen *.686) + (inputBlue * .168)

##outputBlue = (inputRed * .272) + (inputGreen *.534) + (inputBlue * .131)

##c = deepcopy(a)
##d, e, f, gg, sepia = [], [], [], [], []
##for x in range(0, len(c)):
##    aux, aux2, aux3, aux4, aux5 = [], [], [], [], []
##    for y in range(0, len(c[x])):
##        r, g, b = c[x,y]
##        #Escala de grises
##        aux.append(int(r * .299 + g *.587 + b *.114))#Rec. 601
##        aux2.append(int((int(r) + int(g) + int(b))/3)) #Promedio
##        aux3.append(int((max(int(r), int(g), int(b)) #Rango Medio
##            + min(int(r), int(g), int(b)))/2))
##        aux4.append(int(r *.2126 + g *.7152 + b *.0722))#Rec. 709 (HDTV)
##        #Sepia
##        r0 = int((r * .393) + (g *.769) + (b * .189))
##        g0 = int((r * .349) + (g *.686) + (b * .168))
##        b0 = int((r * .272) + (g *.534) + (b * .131))
##
##        r0 = 255 if r0 > 255 else r0
##        g0 = 255 if g0 > 255 else g0
##        b0 = 255 if b0 > 255 else b0
##        aux5.append([r0, g0, b0])
##
##    d.append(aux)
##    e.append(aux2)
##    f.append(aux3)
##    gg.append(aux4)
##    sepia.append(aux5)
##        
##x = np.array(d, dtype=np.uint8)
##Image.fromarray(x.astype(np.uint8)).save("LennaGris.jpg")
##x = np.array(e, dtype=np.uint8)
##Image.fromarray(x.astype(np.uint8)).save("LennaAvg.jpg")
##x = np.array(f, dtype=np.uint8)
##Image.fromarray(x.astype(np.uint8)).save("LennaBrillo.jpg")
##x = np.array(gg, dtype=np.uint8)
##Image.fromarray(x.astype(np.uint8)).save("LennaYUV.jpg")
##x = np.array(sepia, dtype=np.uint8)
##Image.fromarray(x.astype(np.uint8)).save("LennaSepia.jpg")
##
##
##gray = Image.open("LennaSepia.jpg")
##print(gray.size, gray.mode, gray.format)
##
####https://pillow.readthedocs.org/en/3.0.0/reference/Image.html#PIL.Image.Image.convert
####dtype es uint8 para imágenes de 8-bits (0-255) 
##
##
##m_dado = np.asarray(dados, dtype=np.uint8)
##c = deepcopy(m_dado)
##with open("datos.txt", "w") as file:
##    for fila in c:
##        for terna in fila:
##            file.write("({0},{1},{2},{3});"
##                .format(int(terna[0]), int(terna[1]), int(terna[2]), int(terna[3])))
##        file.write("\n")
##
##Image.fromarray(c.astype(np.uint8)).save("prueba.jpg")
img = Image.open("homero.png")
a = np.asarray(img, dtype=np.uint8)
c = deepcopy(a)
for x in range(0, len(c)):
    for y in range(0, len(c[x])):
        x0 = (x-(len(c)/2))
        y0 = (y-(len(c[x])/2))
        r, g, b, a = c[x, y];
        c[x, y] = [int(r), int(g), int(b), 25] if (x0*x0) +(y0*y0) > (120*120) else c[x, y]

Image.fromarray(c.astype(np.uint8)).save("prueba2.png")

####plt.figure()
####plt.subplot(200)
##plt.imshow(a)
####plt.subplot(122)
####plt.imshow(b)
##plt.show()
