from __future__ import division   # fuerza aritmética no entera
import numpy as np                # funciones numéricas (arrays, matrices, etc.)
import matplotlib as plt          # funciones para representación gráfica
from PIL import Image             # funciones para cargar y manipular imágenes

import matplotlib.pyplot as pltpy
import matplotlib.image as mpimg

img = Image.open('Lenna.jpg')
img_png = Image.open('transparencia.png').convert('RGBA')

img2=mpimg.imread('Lenna.jpg')
#img_gray = img.convert('L') #Convertir a escala de grises

##print(img.size, img.mode, img.format)

##http://matplotlib.org/users/image_tutorial.html

a=np.asarray(img, dtype="int32")
b=np.asarray(img_png, dtype=np.uint8)
##print(a[0])
##print(b[0])
##
##print(len(b[0]))
lum_img = img2[:,:,0]
pltpy.imshow(lum_img)
pltpy.show()
pltpy.imshow(lum_img, cmap='hot')
pltpy.show()
##text = ''
##for row in a:
##    for e in row:
##        text += '({}, {}, {}) '.format(e[0], e[1], e[2])
##    text += '\n'
##
####Write the string to a file.
##with open('image.txt', 'w') as f:
##    f.write(text)
##
##
##text = ''
##for row in b:
##    for e in row:
##        text += '({}, {}, {}, {}) '.format(e[0], e[1], e[2], e[3])
##    text += '\n'
##
####Write the string to a file.
##with open('image_png.txt', 'w') as f:
##    f.write(text)





