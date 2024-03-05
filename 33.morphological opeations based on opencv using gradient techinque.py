import cv2
import numpy as np
img=cv2.imread("C:/Users/adich/Downloads/1.jpg",cv2.IMREAD_GRAYSCALE)
kernel=np.ones((5,5),np.uint8)
grad=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
cv2.imshow("original",img)
cv2.imshow("Gradent",grad)
cv2.waitKey(0)
cv2.destoryAllWindows()
