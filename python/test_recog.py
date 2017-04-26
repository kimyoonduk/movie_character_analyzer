
# coding: utf-8

# In[58]:

import face_recognition


# In[75]:

import time


# In[149]:

nic1 = face_recognition.load_image_file('nic1.jpeg')
nicolas_face_encoding = face_recognition.face_encodings(nic1)[0]


# In[147]:

nic2 = face_recognition.load_image_file('nic2.jpeg')
nicolas_face_encoding2 = face_recognition.face_encodings(nic2)[0]


# In[152]:

nicolas_face_encoding


# In[148]:

nicolas_face_encoding2


# In[4]:

unknown = face_recognition.load_image_file('test.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown)[0]


# In[5]:

results = face_recognition.compare_faces([nicolas_face_encoding], unknown_face_encoding)


# In[6]:

results


# In[9]:

new_test = face_recognition.face_encodings(face_recognition.load_image_file('nic9.jpeg'))[0]


# In[10]:

face_recognition.compare_faces([nicolas_face_encoding], new_test)


# In[11]:

pitt_test = face_recognition.face_encodings(face_recognition.load_image_file('pitt.jpg'))[0]


# In[12]:

face_recognition.compare_faces([nicolas_face_encoding], pitt_test)


# In[13]:

side_test = face_recognition.face_encodings(face_recognition.load_image_file('nicside.jpg'))[0]


# In[14]:

face_recognition.compare_faces([nicolas_face_encoding], side_test)


# In[17]:

import cv2
import numpy as np


# In[27]:

import matplotlib.pyplot as plt


# In[140]:

image_list = []


# In[97]:

import os
global image_list

def video_to_frames(video, path_output_dir):
    # extract frames from a video and save to directory as 'x.png' where 
    # x is the frame index
    vidcap = cv2.VideoCapture(video)
    count = 0
    while vidcap.isOpened():
        success, image = vidcap.read()
        if success:
            if(count % 10 == 0):
                image_list.append(image)
                cv2.imwrite(os.path.join(path_output_dir, '%d.png') % count, image)
            count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()



# In[141]:

start_time = time.time()
video_to_frames('basterds.mp4', './basterds')
print("time: " + str(time.time() - start_time))


# In[153]:

len(image_list)


# In[108]:

image_list[250]


# In[154]:

plt.imshow(image_list[230])


# In[155]:

plt.show()


# In[73]:

plt.imshow(nic1)


# In[74]:

plt.show()

