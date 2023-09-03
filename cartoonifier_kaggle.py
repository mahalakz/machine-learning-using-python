# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 23:21:45 2023

@author: mahal
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
original_image=cv2.imread("airport.jpg")
image=cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
# plt.imshow(original_image)

resized1=cv2.resize(image, (960,540))
resized1_gray=cv2.cvtColor(resized1, cv2.COLOR_BGR2GRAY)
# plt.imshow(resized1_gray, cmap='gray')

resized1_gray_smooth=cv2.blur(resized1_gray, (5,5))
# plt.imshow(resized1_gray_smooth, cmap='gray')
lion_edge=cv2.Canny(resized1_gray_smooth, 30, 80)
# plt.imshow(lion_edge, cmap='binary')

getEdge=cv2.adaptiveThreshold(resized1_gray_smooth, 255,
                             cv2.ADAPTIVE_THRESH_MEAN_C,
                             cv2.THRESH_BINARY, 7, 7)
resized2=cv2.resize(getEdge, (960,540))
# plt.imshow(resized2, cmap='gray')

color_image=cv2.bilateralFilter(image,9,300,300)
resized3=cv2.resize(color_image, (960, 540))
# plt.imshow(resized3)
cartoonImage=cv2.bitwise_and(resized3, resized3, mask=getEdge)
resized4=cv2.resize(cartoonImage, (960, 540))
# plt.imshow(resized4)

images=[resized1,resized1_gray,resized1_gray_smooth,resized2,resized3,resized4]

plt.rcParams['figure.figsize']=(10,9)
plt.subplots(3,2)
for i in range(len(images)):
    plt.subplot(3,2,i+1)
    plt.imshow(images[i],cmap='gray')
plt.show()