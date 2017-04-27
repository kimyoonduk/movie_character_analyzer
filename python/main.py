import file_reader
import recognizer

video = "basterds_pub.mp4"
dir_path = "./basterds/"

fr = file_reader.FileReader()

# fr.video_to_frames(video, dir_path)
face_locations = fr.frame_to_numpy_list(dir_path)
print(face_locations)




