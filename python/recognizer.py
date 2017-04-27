# Class for performing facial recognition functions
# take in a numpy array of images to analyze

import face_recognition
#import KHaos

class Recognizer: 

    def __init__(self):
        self.known_face_encodings = []        # should become the trained face encodings
        #self.khaos = khaos()           # khaos class

    def train_classifier(self, training_dir):
        # training steps 
        # currently placeholder
        # TODO: find out how training actually works
       for img in os.listdir(trainingdir):
           encoding = face_recognition.face_encodings(img)
           self.face_encodings.append(encoding)        

    def find_and_recognize(self, face_locations):
        map = { }    # frame : list of actors
        for frame in face_locations:
            unknown_faces = face_recognition.encodings(face_locations)
            for face in unknown_faces:
                for encoding in known_face_encodings:
                    result = face_recognition.compare_faces(encodings, face) 
                    if result:
                        # TODO: put the correct character and frame into map
                        # TODO: find [] index and multiply by 10 for frame num 
                        # TODO: How to find out which character it is?
                        break
        return table
