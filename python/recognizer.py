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
           encoding = face_recognition.face_encodings(img)
           self.known_face_encodings[actor] = encoding
       return self.known_face_encodings


    def test(self, images):
        actor_map = { } # maps frame : list of actors 
        for frame, img in sorted(sorted(images.items()), key=len):
            print(frame)
            frame_face_locations = face_recognition.face_locations(img)
            unknown_faces = face_recognition.face_encodings(img, frame_face_locations)
            if int(frame) > 1500:
                break
            for face in unknown_faces:
                print(face)
                for actor, encoding in self.known_face_encodings.items():
                    result = face_recognition.compare_faces(encoding, face) 
                    print(actor)
                    print(result)
                    if result:
                        print("result was true! found: " + actor)
                        if frame not in actor_map:
                            actors = [actor]
                            actor_map[frame] = actors
                        else:
                            actor_map[frame].append(actor)
                            # actor_map.get(frame) = actor
                    break
        self.khaos.create_actor_map(actor_map)
        return self.khaos


    def find_and_recognize(self, images):
        actor_map = { }    # frame : list of actors
        print("finding face locations")
        face_locations = self.find_face_locations(images)
        print("done finding face locations")
        for index, faces_in_frame in enumerate(face_locations):
            print(index)
            unknown_faces = face_recognition.face_encodings(faces_in_frame)
            for face in unknown_faces:
                for actor, encoding in known_face_encodings.items():
                    result = face_recognition.compare_faces(encoding, face) 
                    frame = index * 10;
                    if result:
                        # todo: is this correct way to check if list contains actor and create new one?
                        if actor_map.get(frame, default=none) != none:
                            actor_map.get(frame).append(actor)
                        else:
                            actors = [actor]
                            actor_map[frame] = actors
                    break
        self.khaos.create_actor_map(actor_map)
        return self.khaos

    def find_face_locations(self, images):
        for img in images.values():
            frame_face_locations = face_recognition.face_locations(img)
            # add the face location to the list 
            self.movie_face_locations.append(frame_face_locations)
        return self.movie_face_locations

