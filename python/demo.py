import file_reader
import recognizer
import khaos
import visualization_factory 

video = "demo.mp4"
dir_path = "./basterds1/"
training_dir = "./training_images/"



fr = file_reader.File_Reader()
recog = recognizer.Recognizer()

#### USE THIS IF YOU WANT TO CREATE EXTRACT THE IMAGE FRAMES FROM THE VIDEO MANUALLY
#fr.video_to_frames(video, dir_path) 



print("Training classifier")
training_images = fr.image_to_array(training_dir, 0)
recog.train_classifier(training_images)
print("TRAINED FACE ENCODINGS!")

print("converting movie images")
movie_images = fr.image_to_array(dir_path, 1)
print("Attempting to find and recognize!")
recog.find_and_recognize(movie_images)
print("Done recognizing: " )

for actor, aos in recog.khaos.aos.items():
    print(actor) 
    print("---------")
    print(len(aos))
    print(aos)

recog.khaos.make_dataframe() 
recog.khaos.save_to_csv("TA_demo.csv")
print("csv file created and stored in ./csv_files/demo.csv")


vf = visualization_factory.Visualization_Factory()
vf.create_visualization(1, recog.khaos, "TA_demo_line")
print("Created line graph!")
print("stored in ./graphs/TA_demo_line.png")

vf.create_visualization(2, recog.khaos, "TA_demo_bar")
print("Created bar plot!")
print("stored in ./graph/TA_demo_bar.png")


