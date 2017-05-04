import file_reader
import recognizer
import time
import khaos
import visualization_factory 

## should replace with the smaller scene
video = "basterds_pub.mp4"

dir_path = "./basterds1/"
training_dir = "./training_images/"



fr = file_reader.FileReader()
recog = recognizer.Recognizer()

# create image frames from video

#### USE THIS IF YOU WANT TO CREATE EXTRACT THE IMAGE FRAMES FROM THE VIDEO MANUALLY
#fr.video_to_frames(video, dir_path) 




###### REAL CODE HERE 
print("Training classifier")
training_images = fr.image_to_array(training_dir, 0)
recog.train_classifier(training_images)
print("TRAINED FACE ENCODINGS!")
print("training time: " + str(time.time() - ovr_st))

con_time = time.time()
print("converting movie images")
movie_images = fr.image_to_array(dir_path, 1)
print("image conversion time: " + str(time.time() - con_time))
print("Attempting to find and recognize!")
recog_time = time.time()
recog.find_and_recognize(movie_images)
print("Done recognizing: " + str(time.time() - recog_time))
print("total time: " + str(time.time() - ovr_st))

for actor, aos in recog.khaos.aos.items():
    print(actor) 
    print("---------")
    print(len(aos))
    print(aos)

recog.khaos.make_dataframe() 
recog.khaos.save_to_csv("demo.csv")
print("csv file created and stored in ./csv_files/demo.csv")




vf = visualization_factory.VisualizationFactory()
vf.create_visualization(1, recog.khaos, "basterds1")
print("Created line graph!")
print("stored in ./graphs/demo.png")


