import cv2

def magic(image):
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray= cv2.cvtColor(gray_image,cv2.COLOR_GRAY2BGR)
    cv2.rectangle(gray, (200,200), (400,400),(192,167,255),2)
    cv2.line(gray, (180,180),(410,180),(255,221,155),2)
    return gray

#capture image from webcam
cam = cv2.VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    cv2.namedWindow("cam-test",flags=cv2.WINDOW_AUTOSIZE)
    cv2.imshow("cam-test",img)
    cv2.waitKey(0)
    cv2.imwrite("cam-test.jpg",img) #save image

#read image from disk
image = cv2.imread("cam-test.jpg")
cv2.imshow("rectangle",magic(image))
cv2.imwrite("gray_image.jpg",magic(image))
cv2.waitKey(0)