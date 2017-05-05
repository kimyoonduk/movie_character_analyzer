import os
import face_recognition
import cv2

class File_Reader:

    """
    extract video to images stored in a dir 
    video: video file path
    path_output_dir: dir to save extracted images
    """
    def video_to_frames(self, video, path_output_dir):
        # extract frames from a video and save to directory as 'x.png' where 
        # x is the frame index
        vidcap = cv2.VideoCapture(video)
        count = 0
        while vidcap.isOpened():
            success, image = vidcap.read()
            if success:
                if(count % 12 == 0):
                    cv2.imwrite(os.path.join(path_output_dir, '%d.png') % count, image)
                if(count % 12000 == 0):
                    print("frame no: " + count)
                count += 1
            else:
                break
        cv2.destroyAllWindows()
        vidcap.release()
        return path_output_dir 

    
    """
    - takes a directory of images and creates:
        - mode 0(training): a dictionary mapping actor : numpy array representations of each image 
        - mode 1(movie images): a dictionary mapping frame number : numpy array representation of each image 
    - dir_path: the dir to read the images from
    """
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


