# 594-s17-project-kimhuangaos
Kim Huang Appearance on Screen Visualizer (khaos visualizer)
https://github.com/cit-upenn/594-s17-project-kimhuangaos

A new way of visualizing movies 
## Main Idea
- takes a video file and extracts still-frame-images of the video
- converts the image files to a list of numpy arrays representing each image
- Using training images, the classifier will provide an encoding for our training images that can be used to detect and recognize faces.
	- the facial recognition classifer uses dlib
- Using the classfier, run each numpy array represented image from a movie and store the appearance of each actor for each frame. 
	- stored as a dictionary that maps each frame index : dictionary of actors mapped to a list of hits/misses(1/0) 
	- output looks like this:
	
	frame|actor1|actor2|actor-n
	-----|------|------|-------
	0  	 | 0	| 1    | 1
	1	 | 0    | 0    | 1
	2	 | 1	| 1	   | 1
	3    | 1	| 1    | 1

- convert the stored data into a dataframe for visualization processing.
- Use the dataframe to create a line plot and a bar plot 

## How face detection and recognition works
- how face detection works:
	1. Histogram of Gradients
		- convert image to black and white
		- look at each pixel or a small grouping of pixels, say 16x16, to determine the direction of light to dark across an image.
		- This allows for all images to be represented the same way, regardless if it is a dark or light picture 
		- Now we can look look at an unknown picture and determine if its HOG pattern shares any similarity from HOG patterns extracted from training images
- how face recognition works:
	1. Face Landmark Estimation
		- deals with faces that aren't directly centered by adjusting the picture to line up eyes and lips in the same place every time
		- use landmarks, or 68 specific points on a face that a machine learning algorithm can be trained to recognize on any face 
	2. Encoding
		- train a Deep Convolutional Neural network to recognize and measure 128 measurements on each face
			1. Use 3 images at a time for training, 2 of the same known person and 1 of a different person
			3. The neural network will do machine-learning things to make sure the measurements it generates for image 1 and image 2 of the same person are closer, while the measurements between the known person and the different person are slightly further apart
		- Now the trained neural network can produce almost identical numbers for the 128 measurement when looking at different pictures of the same person
		- By comparing the similarity of two encodings, we can determine if we know the person who appears in the image

# run our demo! (demo.py) 
- run this to get shortened and preconfigured version of our product from start to finish
- run in command line with no extra arguments
- it defaults to just using the still-frames. If you want to perform the video extraction as well uncomment line 19
- these are the dependencies:
	- Python3
	- OpenCV
	- Dlib
	- A dlib wrapper library called face_recognition 
		- https://github.com/ageitgey/face_recognition 
	- pandas
	- matplotlib 
	- seaborn

## Issues we dealt with
- During testing, we discovered that some frames did not recognize all of the faces. 
	- after some research and testing we found that the library we used, dlib, is not very good at dealing with sidefaces. In some frames it would not recognize that a face existed if it was from too much of a side angle
- A few false postitive would occur as well if two actors were similar in facial structure. We tried adjust for different thresholds of similarity and found that 0.6 gave the best results. 


## FileReader
- video_to_frames(self, video, path_output_dir)
	- use openCV to extract video frames and store as images for further processing
		- reads every 12 frames because video is often 24fps. Gives us a captured frame every 0.5s
- image_to_array(self, dir_path, mode)
	- takes a directory of images and creates:
		1. a dictionary mapping actor : numpy array representations of each image 
		2. a dictionary mapping frame number : numpy array representation of each image
	- used for both the training images and for the movie frames
		- mode 0 for training images
		- mode 1 for movie images
	 
## Recognizer
- train_classifier(self, images)
	- takes in a dictionary of actor : numpy arrays that represent the images
	- encodes each actor's specific facial landmarks 
	- return: dictionary of actors mapped to trained-face-encodings called known_face_encodings
- find_and_recognize(self, images)
	- takes in a dictionary of actor : numpy arrays that represent the images
	1. go through movie frames and detects each face present
	2. create an encoding for each unknown face
	3. compares each unknown face encoding to our mapping of known_face_encodings 
		- if the difference between the encodings is below the threshold of 0.6, then we have found our actor
	4. store the results in our data container class, Khaos
	- return: khaos (storage class)

## Khaos
- Data storage class
	- stores a dictionary called apperance on screen (aos) that maps each frame index : dictionary of actors mapped to a list of hits/misses(1/0) 
	- output looks like this:
	
	frame|actor1|actor2|actor-n
	-----|------|------|-------
	0  	 | 0	| 1    | 1
	1	 | 0    | 0    | 1
	2	 | 1	| 1	   | 1
	3    | 1	| 1    | 1
- zero_aos(self, actor)
	- initializes all values to 0
	- this way we only have to change values to 1 on a hit
- mark_aos(self, actor, frame_index)
	- marks that an actor has appeared on the screen at this frame
- make_dataframe(self)
	- creates a pandas dataframe datastructure to allow for better visualization construction
- save_to_csv(self, filepath)
	- saves the khaos data to a csv file so we can perform visualization from this step if desired

## VisualizationFactory
- create_visualizer(self, khaos, mode, filename)
	- a factory method
	- define the type of visualization we want to create and use attributes of khaos to create the desired graph
	- Can create a line graph visualization, or an animation visualization

## Visualizer_line
- creates the line graph visualization of the data

## Visualizer_bar
- creates a bar plot visualization of the data


#### Work Breakdown
- Combo: Research, design, idea formulation, and testing
- YD: Visualization and video extraction 
- Jon: Facial recognition, training, image conversion
