# Class for performing facial recognition functions
# take in a numpy array of images to analyze

import face_recognition
import khaos

class Recognizer: 

    def __init__(self):
        self.known_face_encodings = { } # should become the trained face encodings
        self.movie_face_locations = []
        self.khaos = khaos.Khaos()           

    def train_classifier(self, images):
        # training steps 
        # TODO: find out how training actually works
        # TODO: is one training image enough?
       for actor, img in images.items():
           encoding = face_recognition.face_encodings(img)[0]
           self.known_face_encodings[actor] = encoding
           self.khaos.actors[actor] = []

       return self.known_face_encodings


    def find_and_recognize(self, images):
        actor_map = { } # maps frame : list of actors 
        counter = 0
        for frame in sorted(images, key=int):
            print(frame)
            # frame_face_locations = face_recognition.face_locations(img)
            # unknown_faces = face_recognition.face_encodings(img, frame_face_locations)
            unknown_faces = face_recognition.face_encodings(images[frame])
            # TODO: issue is it's not recognizing side faces
            print("unknown_faces len: " + str(len(unknown_faces)))
            #if int(frame) > 1500:
            #    break

            for actor, aos in self.khaos.actors.items():
                self.khaos.actors[actor].append(0)

            for face in unknown_faces:
                for actor, encoding in self.known_face_encodings.items():
                    results = face_recognition.compare_faces([encoding], face) 
                    print(actor)
                    print("results len: " + str(len(results)))
                    print(results)
                    if True in results:
                        ## printing results says false but still enters here
                        print("result was true! found: " + actor)
                        self.khaos.actors[actor][counter] = 1

           
            counter += 1
                

#        self.khaos.create_actor_map(actor_map)
        for actor, aos in self.khaos.actors.items():
            print(actor) 
            print("---------")
            print(len(aos))
            print(aos)

        return self.khaos


