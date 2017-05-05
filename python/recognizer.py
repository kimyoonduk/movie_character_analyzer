# Class for performing facial recognition functions
# take in a numpy array of images to analyze

import face_recognition
import khaos

class Recognizer: 

    '''
    constructor
    creates a dictionary of known face encodings and an empty khaos object
    '''
    def __init__(self):
        self.known_face_encodings = { } # should become the trained face encodings
        self.khaos = khaos.Khaos()           

    '''
    trains classifier with given images of actors and saves them as dictionary of name, image pairs
    images = input images 
    '''
    def train_classifier(self, images):
       for actor, img in images.items():
           encoding = face_recognition.face_encodings(img)[0]
           self.known_face_encodings[actor] = encoding
           self.khaos.aos[actor] = []

       return self.known_face_encodings


    '''
    runs through the image file to find and recognize faces if there is any
    compares each faces with known face encodings to match with actors
    images = input images
    '''
    def find_and_recognize(self, images):
        frame_index = 0
        for frame in sorted(images, key=int):
            print()
            print("FRAME: " + frame)

            unknown_faces = face_recognition.face_encodings(images[frame])
            print("unknown_faces len: " + str(len(unknown_faces)))

            for actor, aos in self.khaos.aos.items():
                # self.khaos.aos[actor].append(0)
                self.khaos.zero_aos(actor)

            for face in unknown_faces:
                for actor, encoding in self.known_face_encodings.items():
                    ## can test with different tolerance 
                    # default is 0.6
                    results = face_recognition.compare_faces([encoding], face, tolerance=0.6)
#                    print(actor)
#                    print("results len: " + str(len(results)))
#                    print(results)
                    if True in results:
                        print("result was true! found: " + actor)
                        # self.khaos.aos[actor][counter] = 1
                        self.khaos.mark_aos(actor,frame_index)

            frame_index += 1
                
        return self.khaos


