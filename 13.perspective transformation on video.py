import cv2
import numpy as np

cap = cv2.VideoCapture("C:/Users/adich/Downloads/indian-cricket-team-whatsapp-status-video-2021.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    pts1 = np.float32([[200, 300], [5, 2], [0, 4], [6, 0]])
    pts2 = np.float32([[0, 0], [4, 0], [0, 1], [4, 6]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (frame.shape[1], frame.shape[0]))

    cv2.imshow('frame', frame)  
    cv2.imshow('frame1', result)  

    if cv2.waitKey(24) == 27:
        break

cap.release()
cv2.destroyAllWindows()
                        
                     
