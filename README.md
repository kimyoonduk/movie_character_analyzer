# 594-s17-project-kimhuangaos


## demo.py 
- run this to get shortened version of our product from start to finish

## Main Idea
- takes in a video file and extracts still-frame-images of the videos
- converts the image files to a list of numpy arrays representing each image
- Using training images, train the classifier to detect and recognize faces, properly attributing each face to the correct actor
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
- Use the dataframe to create a line graph and an animated graph

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
	- return: khaos 

## Khaos
- Data storage class
	- stores a dictionary that maps each frame index : dictionary of actors mapped to a list of hits/misses(1/0) 
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
- creates the line graph visualization of data

## Visualizer_Animation
