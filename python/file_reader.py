import os
import face_recognition
import cv2

global image_list

class FileReader:

    def __init__(self):
        self.face_locations = []
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


    # TODO: create function for reading the dir where the .png files are created
    def frame_to_numpy_list(self, dir_path):
        # TODO os.listdir accesses files in random order ***Solved*** 
        for img in sorted(sorted(os.listdir(dir_path)), key=len):
            img_path = dir_path + img
            if (os.path.isfile(img_path)):
                print(img)
               ## image = face_recognition.load_image_file(img_path)
               ## frame_face_locations = face_recognition.face_locations(image)
                # add the face location to the list 
               ## self.face_locations.append(frame_face_locations)
       ## return self.face_locations



