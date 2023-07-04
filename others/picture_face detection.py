# //Face Detection Code

# //import the necessary packages
!pip install face_recognition
import cv2

#load the input image and convert it to grayscale
image = cv2.imread("Bikman.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#load the pre-trained face detector
# detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#detect faces in the image
faces = detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

#loop over the detected faces
for (x,y,w,h) in faces:
	#draw a rectangle around the face
	cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)

#show the output image
cv2.imshow("Faces Found", image)
cv2.waitKey(0)

#Face Recognition Code

#import the necessary packages
import face_recognition

#load the input image and convert it to RGB
image = face_recognition.load_image_file("Bikman.jpg")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#detect the (x, y)-coordinates of the bounding boxes
#corresponding to each face in the input image
boxes = face_recognition.face_locations(rgb, model="hog")

#loop over the bounding boxes
for (top, right, bottom, left) in boxes:
	#draw the bounding box on the image
	cv2.rectangle(image, (left, top), (right, bottom), (0,0,255), 2)

#show the output image
cv2.imshow("Faces Found", image)
cv2.waitKey(0)

# Name and Image of Owner Found in Webcam

# Name: John Smith
# Image: https://www.pexels.com/photo/man-wearing-black-leather-jacket-and-blue-jeans-standing-on-gray-concrete-surface-1597008/