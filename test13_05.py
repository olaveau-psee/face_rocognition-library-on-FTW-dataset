
import face_recognition

import os
import PIL
from PIL import Image,ImageDraw
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


test = Image.open('/home/olivia/Documents/FTW_facedetection/originalPics/2002/07/19/big/img_408.jpg') 

image = face_recognition.load_image_file("/home/olivia/Documents/FTW_facedetection/originalPics/2002/07/19/big/img_408.jpg")
face_locations = face_recognition.face_locations(image)
amount = len(face_locations)
print(f'There are {amount} face locations')
first_face_location = face_locations[0]
print(first_face_location)
img = Image.fromarray(image, 'RGB')
img_with_red_box = img.copy()
img_with_red_box_draw = ImageDraw.Draw(img_with_red_box)
img_with_red_box_draw.rectangle(
    [
        (first_face_location[3], first_face_location[0]),
        (first_face_location[1], first_face_location[2])
    ],
    outline="red",
    width=3
)
img_with_red_box.show()


#<major_axis_radius minor_axis_radius angle center_x center_y 1>.
#<left_x top_y width height detection_score> 

