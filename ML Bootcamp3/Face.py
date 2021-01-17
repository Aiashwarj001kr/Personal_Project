import cv2

cam = cv2.VideoCapture(0)

while True:
    ret,frame = cam.read()
    if ret==False:
        continue

    #Display the capture video
    cv2.imshow("Cams",frame)
    
    #Use ESC key to close "Cams Window"
    if cv2.waitKey(1) & 0xFF == 27 :
        break

cam.release()
cv2.destroyAllWindows()
