# Class for performing facial recognition functions
# take in a numpy array of images to analyze

import face_recognition
#import KHaos

class Recognizer: 
#    face_encodings
#    KH = khaos

    def __init__(self):
        self.face_encodings = []        # should become the trained face encodings
        #self.khaos = khaos()           # khaos class

    def train_classifier(self, training_dir):
       # training steps 
       self.face_encodings.append(0)        # placeholder

    def find_and_recognize(self, numpy):
        for frame in numpy:
            facial_recognition.compare_faces(numpy[frame], face_encodings)
            
