import cv2
import pyautogui

face_cascade = cv2.CascadeClassifier('face.xml')
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    _, img = cap.read()
    if _ == True:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray,1.9,4)
        for (x, y, w, h) in face:
            cv2.rectangle(img, (x,y), (x+w,x+h),(225,0,0),2)
            # pyautogui.moveTo(x,y,duration=0.5)
        cv2.imshow("img",img)

        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
