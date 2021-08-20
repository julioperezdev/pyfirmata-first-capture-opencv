import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)
rectangleColor = 255

while True:
    _, image = capture.read()
    grayColor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayColor, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(
            image,
            (x, y),
            (x+w, y+h),
            (rectangleColor, 0, 0),
            2)
    cv2.imshow('img', image)
    checkIfSettingKeycap = cv2.waitKey(30)
    if checkIfSettingKeycap == 27:
        break
capture.release()