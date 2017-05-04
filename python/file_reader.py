import os
import face_recognition
import cv2

global image_list

class FileReader:

    def __init__(self):
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
                if(count % 12 == 0):
                    global image_list
                    image_list.append(image)
                    cv2.imwrite(os.path.join(path_output_dir, '%d.png') % count, image)
                if(count % 12000 == 0):
                    print("frame no: " + count)
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
            if (".DS_Store" in img_path):
                continue
            if (os.path.isfile(img_path)):
                # store map of filename : image tuple
                # OR actor : image
                image_arr = face_recognition.load_image_file(img_path)
                if mode == 0:
                    actor_name = img.split(".")[0]
                    print("converting " + actor_name)
                    image_map[actor_name] = image_arr 
                else: 
                    frame = img.split(".")[0]
                    image_map[frame] = image_arr
        return image_map


