# Class for performing facial recognition functions
# take in a numpy array of images to analyze

import face_recognition
import khaos

class Recognizer: 

    def __init__(self):
        # TODO: Decide if it should be a dictionary of <actor_name : encoding>
        self.known_face_encodings = { } # should become the trained face encodings
        self.khaos = khaos.Khaos()           

    def train_classifier(self, training_list):
        # training steps 
        # currently placeholder
        # TODO: find out how training actually works
        # TODO: is one training image enough?
       for img in image_list:
           encoding = face_recognition.face_encodings(img)
           self.face_encodings.append(encoding)        

    def find_and_recognize(self, face_locations):
        actor_map = { }    # frame : list of actors
        for index, faces_in_frame in enumerate(face_locations):
            # Docs make it seem like I have to pass in an image here?
            # I am trying to just pass in a numpy arr of face locations
            unknown_faces = face_recognition.face_encodings(faces_in_frame)
            for face in unknown_faces:
                for actor, encoding in known_face_encodings.items():
                    result = face_recognition.compare_faces(encoding, face) 
                    frame = index * 10;
                    if result:
                        # TODO: is this correct way to check if list contains actor and create new one?
                        if actor_map.get(frame, default=None) != None:
                            actor_map.get(frame).append(actor)
                        else:
                            actors = [actor]
                            actor_map[frame] = actors
                    break
        self.khaos.create_actor_map(actor_map)
        return self.khaos

