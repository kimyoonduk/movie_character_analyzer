# 594-s17-project-kimhuangaos


## Issues we dealt with
- The library we used, dlib, is not very good at dealing with sidefaces. Certain frames it would not recognize that a face existed if it was from too much of a side angle

# FileReader
- video_to_frames()
	- use openCV to extract video frames and store as images for further processing
		- reads every 12 frames because video is often 24fps. Gives us a captured frame every 0.5s
- image_to_array()
	- takes a directory of images and creates a list of numpy array representations of each image 
	- used for both the training images and for the movie frames
	 
# Recognizer
- train_classifier()
	- provide a directory of training images in order to train our classifier to recognize different actors based on their specific facial landmarks
	- return: dictionary of actors mapped to trained-face-encodings 
- find_and_recognize()
	- go through movie frames and detect actors in each frame
	- return: khaos 

# Khaos
- Data storage class
- 

## VisualizationFactory
- contains a factory method create_visualizer(self, khaos, type, filename)
	- define the type of visualization we want to create and make it uses attributes of khaos

# Visualizer_line

