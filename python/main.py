import file_reader
import recognizer
import time

video = "basterds_pub.mp4"
dir_path = "./basterds/"
training_dir = "./training_images/"

fr = file_reader.FileReader()
recog = recognizer.Recognizer()

ovr_st = time.time()
# create image frames from video
### fr.video_to_frames(video, dir_path)


###### REAL CODE HERE
print("Training classifier")
training_images = fr.image_to_array(training_dir, 0)
recog.train_classifier(training_images)
print("TRAINED FACE ENCODINGS!")
print("training time: " + str(time.time() - ovr_st))
#print(recog.known_face_encodings)

con_time = time.time()
print("converting movie images")
movie_images = fr.image_to_array(dir_path, 1)
print("image conversion time: " + str(time.time() - con_time))
print("Attempting to find and recognize!")
recog_time = time.time()
# recog.find_and_recognize(movie_images)
recog.find_and_recognize(movie_images)
print("Done recognizing: " + str(time.time() - recog_time))
print("total time: " + str(time.time() - ovr_st))
actor_map = recog.khaos.get_actor_map() 
print(actor_map)

"""
#### TEST CODE BELOW
diane_train_img = fr.image_to_array("diane/", 0)
recog.train_classifier(diane_train_img)
print("printing known encoding: ")
print(recog.known_face_encodings)
movie_images = fr.image_to_array("diane_test/", 1)
recog.find_and_recognize(movie_images)
#actor_map = recog.khaos.get_actor_map()
#print(actor_map)
"""
