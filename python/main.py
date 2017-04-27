import file_reader
import recognizer

video = "basterds_pub.mp4"
dir_path = "./basterds/"
training_dir = "./training_images/"

fr = file_reader.FileReader()
recog = recognizer.Recognizer()

# create image frames from video
### fr.video_to_frames(video, dir_path)

### face_locations = fr.frame_to_numpy_list(dir_path)
### print(face_locations)

mapping = fr.train(training_dir)
print(mapping)

### training_list = fr.frame_to_numpy_list(training_dir)
### recog.train_classifier(training_list)
### print(recog.face_encodings)
### print(recog.khaos)
### recog.find_and_recognize(face_locations)


