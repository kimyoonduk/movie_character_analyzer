import face_recognition
#import dlib

print("Hi")
image = face_recognition.load_image_file("Will_Ferrell.jpg");
face_locations = face_recognition.face_locations(image)
print(face_locations)
