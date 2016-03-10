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
##https://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale

##outputRed = (inputRed * .393) + (inputGreen *.769) + (inputBlue * .189)

##outputGreen = (inputRed * .349) + (inputGreen *.686) + (inputBlue * .168)

##outputBlue = (inputRed * .272) + (inputGreen *.534) + (inputBlue * .131)

c = deepcopy(a)
d=[]
e=[]
f=[]
gg=[]
sepia = []
for x in range(0, len(c)):
    aux = []
    aux2=[]
    aux3=[]
    aux4 =[]
    aux5 = []
    for y in range(0, len(c[x])):
        r, g, b = c[x,y]
        var = r*(299/1000) + g*(587/1000) + b*(114/1000)
        var2 = (int(r) + int(g) + int(b))/3
        var3 = (max(int(r), int(g), int(b)) + min(int(r), int(g), int(b)))/2
        var4 = r*(0.2126) + g*(0.7152) + b*(0.0722)
        r0 = int((r * .393) + (g *.769) + (b * .189))
        g0 = int((r * .349) + (g *.686) + (b * .168))
        b0 = int((r * .272) + (g *.534) + (b * .131))
        if r0 > 255:
            r0 = 255
        if g0 > 255:
            g0 = 255
        if b0 > 255:
            b0 = 255
        aux.append(int(var))
        aux2.append(int(var2))
        aux3.append(int(var3))
        aux4.append(int(var4))
        aux5.append([r0, g0, b0])
    d.append(aux)
    e.append(aux2)
    f.append(aux3)
    gg.append(aux4)
    sepia.append(aux5)
        
x = np.array(d, dtype=np.uint8)
Image.fromarray(x.astype(np.uint8)).save("LennaGris.jpg")
x = np.array(e, dtype=np.uint8)
Image.fromarray(x.astype(np.uint8)).save("LennaAvg.jpg")
x = np.array(f, dtype=np.uint8)
Image.fromarray(x.astype(np.uint8)).save("LennaBrillo.jpg")
x = np.array(gg, dtype=np.uint8)
Image.fromarray(x.astype(np.uint8)).save("LennaYUV.jpg")
x = np.array(sepia, dtype=np.uint8)
Image.fromarray(x.astype(np.uint8)).save("LennaSepia.jpg")

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
