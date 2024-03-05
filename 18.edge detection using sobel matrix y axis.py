import cv2
img=cv2.imread("C:/Users/adich/Downloads/1 mask.jpeg")
cv2.imshow('original',img)
cv2.waitKey(0)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur=cv2.GaussianBlur(img_gray,(3,3),0)
sobely=cv2.Sobel(src=img_blur,ddepth=cv2.CV_64F,dx=0,dy=1,ksize=5)
cv2.imshow('sobel Y',sobely)
cv2.waitKey(0)
