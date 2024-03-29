import cv2
main_image = cv2.imread("C:/Users/adich/Downloads/1.jpg")
insert_image = cv2.imread("C:/Users/adich/Downloads/2.jpg")
insert_image = insert_image[50:200, 50:200]
rows, cols, channels = insert_image.shape
roi = main_image[50:50+rows, 50:50+cols]
inserted_image = cv2.addWeighted(roi, 0.5, insert_image, 0.5, 0)
main_image[50:50+rows, 50:50+cols] = inserted_image
cv2.imshow('Result', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
