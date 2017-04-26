import file_reader
import recognizer

file_reader = File_Reader()


video = "video.mp4"
path_output_dir = "./basterds"
file_reader.file_reader.video_to_frames(video, path_output_dir)


