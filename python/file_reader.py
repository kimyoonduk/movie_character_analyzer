import os
import facial_recognition
global image_list

class File_Reader:

    def __init__(self):
        self.face_locations = []

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
                    image_list.append(image)
                    cv2.imwrite(os.path.join(path_output_dir, '%d.png') % count, image)
                count += 1
            else:
                break
        cv2.destroyAllWindows()
        vidcap.release()
        return path_output_dir 

    # TODO: create function for reading the dir where the .png files are created
    def frame_to_numpy_arr(self, dir_path):
        for img in os.listdir('\'' + dir_path + '\''):
            if (os.path.isfile(img)):
                image = face_recognition.load_image_file(img)
                frame_face_locations = face_recognition.face_locations(image)
                # add the face location to the list 
                self.face_locations.append(frame_face_locations)
        return self.face_locations



