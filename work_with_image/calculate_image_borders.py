# Загрузите изображение из файла img.png. 
# Изображение состоит из рамки сплошного цвета и внутренней части изображения. 
# Цвет рамки можно узнать, посмотрев на левый верхний пиксель. 
# Рамка может иметь разную ширину со всех четырех сторон.
# Определите размеры рамки и выведите эти размеры через пробел.
# Размеры рамки выводите в следующем порядке: левый, верхний, правый, нижний.

from skimage.io import *
import numpy as np

img = imread('img.png')
a=[]

for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        if np.all(img[row,col]!=img[0, 0]):
            a.append((row,col))
            
print(a[0][1], a[0][0], img.shape[1] - a[-1][1] - 1, img.shape[0] - a[-1][0] - 1)