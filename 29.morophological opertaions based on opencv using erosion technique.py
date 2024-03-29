import cv2
import numpy as np
image_path = "C:/Users/adich/Downloads/1 mask.jpeg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)  
eroded_image = cv2.erode(image, kernel, iterations=1)
cv2.imshow('Original', image)
cv2.imshow('Eroded', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
