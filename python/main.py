import file_reader
import recognizer
import time
import khaos
import visualization_factory 

#video = "basterds_pub.mp4"
# video = "/Users/ydkim/Prog/594_p2/python/crazy.mp4"
# dir_path = "./starwars0/"
# training_dir = "./starwars_train/"

dir_path = "./basterds1/"
training_dir = "./training_images/"



fr = file_reader.File_Reader()
recog = recognizer.Recognizer()

ovr_st = time.time()
# create image frames from video

#fr.video_to_frames(video, dir_path)



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

for actor, aos in recog.khaos.aos.items():
    print(actor) 
    print("---------")
    print(len(aos))
#    print(aos)

recog.khaos.make_dataframe()
recog.khaos.save_to_csv("basterds1.csv")
print("csv file created!")

"""
## test factory starting at csv starting from here
kh = khaos.Khaos()
kh.get_df_from_csv("basterds1.csv")
"""

vf = visualization_factory.Visualization_Factory()
#vf.create_visualization(1, kh, "basterds1_test2")
vf.create_visualization(1, recog.khaos, "basterds1_line")
print("Created line graph!")
vf.create_visualization(2, recog.khaos, "basterds1_bar")
print("Created bar plot!")
print("look for visualizations inside of ./graphs/")



"""
#### TEST CODE BELOW
# diane_train_img = fr.image_to_array("diane/", 0)
# recog.train_classifier(diane_train_img)

training_images = fr.image_to_array(training_dir, 0)
recog.train_classifier(training_images)
movie_images = fr.image_to_array("diane_test/", 1)
recog.find_and_recognize(movie_images)

for actor, aos in recog.khaos.aos.items():
    print(actor) 
    print("---------")
    print(len(aos))
    print(aos)

recog.khaos.make_dataframe()
recog.khaos.save_to_csv("test")
print("csv file created!")

"""
