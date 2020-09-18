import cv2
import numpy as np
def nothing(x):pass

faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cv2.namedWindow('sketch (Press S to save)', cv2.WINDOW_NORMAL)
cv2.createTrackbar('Trackbar','sketch (Press S to save)',0,255,nothing)

while(True):
    ret, frame = cap.read()
    vid_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face = faces.detectMultiScale(vid_gray, 1.3, 5)
    
    thresh = cv2.getTrackbarPos('Trackbar','sketch (Press S to save)');
    img_blur = cv2.GaussianBlur(vid_gray,(7,7),0)
    canny_edges = cv2.Canny(img_blur,thresh,thresh+10)
    
    vid_bw = cv2.threshold(canny_edges, thresh, 255, cv2.THRESH_BINARY_INV)[1]
    for x,y,w,h in face:
        cv2.rectangle(vid_bw,(x-(x//2),y-(y//3)),(x+(w+(w//2)),y+(h+(h//2))),(255,0,0),2)
        img = vid_bw[y-(y//3):y+(h+(h//2)),x-(x//2):(x+(w+(w//2)))]
        face_image = cv2.flip(img,1)  
    
    cv2.imshow('sketch (Press S to save)',cv2.flip(vid_bw,1))
       
    if cv2.waitKey(30) & 0xFF == ord('s'):
        cv2.imwrite("sketch.jpg",face_image)
        break

cap.release()
cv2.destroyAllWindows()
