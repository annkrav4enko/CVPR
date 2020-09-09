import cv2
import time
from main import magic

capture_duration = 5
cap= cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('color_output.avi',fourcc, 20.0, (640,480))
#capture video from webcam
start_time = time.time()
while( int(time.time() - start_time) < capture_duration ):
    ret, frame = cap.read()
    if ret==True:
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        out.write(frame)
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

#import video
out2=cv2.VideoWriter('gray_output.avi',fourcc, 20.0, (640,480))
capture=cv2.VideoCapture("color_output.avi")
while(capture.isOpened()):
    ret,frame = capture.read()
    if ret==True:
        out2.write(magic(frame))
        cv2.imshow('frame', magic(frame))
        cv2.waitKey(40)
    else:
        break
capture.release()
out2.release()
