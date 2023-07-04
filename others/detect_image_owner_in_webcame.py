#importing libraries
import cv2
import face_recognition

#loading the image
image = face_recognition.load_image_file("Bikman.jpg")

#finding the face in the image
face_locations = face_recognition.face_locations(image)

#finding the face encodings
face_encodings = face_recognition.face_encodings(image, face_locations)

#loading the webcam
video_capture = cv2.VideoCapture(0)

#looping through the frames
while True:
    #grabbing the frame
    ret, frame = video_capture.read()

    #finding the face locations in the frame
    face_locations = face_recognition.face_locations(frame)

    #finding the face encodings in the frame
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    #looping through the face encodings
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        #comparing the face encodings
        matches = face_recognition.compare_faces([face_encoding], face_encodings)

        #checking if the face is a match
        if True in matches:
            #displaying the name and image of the owner
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, "Owner", (left, top - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.imshow('Owner', image)

    #displaying the frame
    cv2.imshow('Video', frame)

    #breaking the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#releasing the webcam
video_capture.release()
cv2.destroyAllWindows()