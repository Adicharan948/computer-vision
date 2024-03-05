import cv2
import numpy as np
img = cv2.imread("C:/Users/adich/Downloads/imh.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
laplacian_kernel=np.array([[0,1,0],[1,-4,1],[0,1,0]])
laplacian=cv2.filter2D(gray,-1,laplacian_kernel)
sharpened=cv2.add(gray,laplacian)
cv2.imshow('original image',gray)
cv2.imshow('sharpened image',sharpened)
cv2.waitkey()
cv2.destoryAllWindows()
