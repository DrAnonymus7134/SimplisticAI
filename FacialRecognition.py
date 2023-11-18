import cv2
width = 640 # Change this to your preferred width
height = int(width * 0.5625)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 60)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade = cv2.CascadeClassifier('Haar\haarcascade_frontalface_default.xml') # You might need to change this to the path where you put the file

while True:
    ignore, frame = cam.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray, 1.3, 5) # The second digit shows how much you trust the AI. Try changing it if the script is acting weird

    for face in faces:
        x, y, w, h = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    cv2.imshow('my Webcam', frame)
    cv2.moveWindow('my Webcam', 0, 0) # Change these last two digits to where you want the picture
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
