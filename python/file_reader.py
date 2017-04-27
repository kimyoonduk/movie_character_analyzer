import os
import face_recognition
import cv2

global image_list

class FileReader:

    def __init__(self):
        self.movie_face_locations = []
        global image_list 
        image_list = []

    # extract video to images stored in a dir
    def video_to_frames(self, video, path_output_dir):
        # extract frames from a video and save to directory as 'x.png' where 
        # x is the frame index
        vidcap = cv2.VideoCapture(video)
        count = 0
        while vidcap.isOpened():
            success, image = vidcap.read()
            if success:
                if(count % 10 == 0):
                    global image_list
                    image_list.append(image)
                    cv2.imwrite(os.path.join(path_output_dir, '%d.png') % count, image)
                count += 1
            else:
                break
        cv2.destroyAllWindows()
        vidcap.release()
        return path_output_dir 

    def get_image_list(self):
        global image_list
        return image_list

    """  mode 0 = training
         mode 1 = analysis """
    def image_to_array(self, dir_path, mode):
        image_map = { }
        for img in sorted(sorted(os.listdir(dir_path)), key=len):
            img_path = dir_path + img
            if (os.path.isfile(img_path)):
                # store map of filename : image tuple
                # OR actor : image
                image_arr = face_recognition.load_image_file(img_path)
                if mode == 0:
                    actor_name = img.split(".")[0].replace("_", " ")
                    image_map[actor_name] = image_arr 
                else: 
                    frame = img.split(".")[0]
                    image_map[frame] = image_arr
        return image_map

    def frame_to_face_locations(self, dir_path):
        # TODO os.listdir accesses files in random order ***Solved*** 
        for img in sorted(sorted(os.listdir(dir_path)), key=len):
            img_path = dir_path + img
            if (os.path.isfile(img_path)):
                image = face_recognition.load_image_file(img_path)
                frame_face_locations = face_recognition.face_locations(image)
                # add the face location to the list 
                self.movie_face_locations.append(frame_face_locations)
        return self.movie_face_locations


    def train(self, training_dir):
       encoding_map = { }
       for img in os.listdir(training_dir):
           img_path = training_dir + img
           actor_name = img.split(".")[0].replace("_", " ")
           face = face_recognition.load_image_file(img_path)
           encoding = face_recognition.face_encodings(face)
           encoding_map[actor_name] = encoding
       return encoding_map 


