import file_reader
import recognizer

video = "basterds_pub.mp4"
path_output_dir = "./basterds"

fr = file_reader.FileReader()

fr.video_to_frames(video, path_output_dir)


