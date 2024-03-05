import cv2
import numpy as np
img=cv2.imread("C:/Users/adich/Downloads/1 mask.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kernel=np.array([[0,1,0],[1,-8,1],[0,1,0]])
sharpened=cv2.filter2D(gray,-1,kernel)
cv2.imshow('original',gray)
cv2.imshow('sharpened',sharpened)
cv2.waitKey(0)
cv2.destoryAllWindows()
