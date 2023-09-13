from cv2 import cv2
import face_recognition

image = face_recognition.lead_image_file('1.jpeg')
image = cv2.cvtColor(image.cv2.COLOR_BGR2RGB)

cv2.imshow('image', image)
cv2.waitKey(0)
