import face_recognition

import os
import PIL
from PIL import Image,ImageDraw
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# path
images_directory = '/home/olivia/Documents/FTW_facedetection/originalPics/2002/07/19/big/'

# all files in the repertory
images_list = os.listdir(images_directory)

for image_name in images_list:
    image_path = os.path.join(images_directory, image_name)
    try:
        image = face_recognition.load_image_file(image_path)
        
        # Detection
        face_locations = face_recognition.face_locations(image)
        amount = len(face_locations)
        print(f'In {image_name}, there is {amount} face(s)')
        
        # Draw lines around the face(s)
        img = Image.fromarray(image, 'RGB')
        draw = ImageDraw.Draw(img)
        for face_location in face_locations:
            draw.rectangle([(face_location[3], face_location[0]), (face_location[1], face_location[2])], outline="red", width=3)
        
        img_np = img.convert("RGB")
        
        plt.imshow(img_np)
        plt.axis('off')  # Masquer les axes
        plt.show()
        
    except Exception as e:
        print(f"ERROR {image_name}: {e}")

