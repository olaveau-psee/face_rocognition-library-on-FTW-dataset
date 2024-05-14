
import os
import face_recognition
import PIL
from PIL import Image,ImageDraw
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


images_directory = '/home/olivia/Documents/FTW_facedetection/originalPics/2002/07'

txt_file_directory = '/home/olivia/Documents/FTW_facedetection//FDDB-folds/alltogether.txt'

def parcourir_dossiers(dossier):
    chemins_images = []
    for element in os.listdir(dossier):
        element_path = os.path.join(dossier, element)
        if os.path.isdir(element_path):
            chemins_images.extend(parcourir_dossiers(element_path))
        else:
            if element.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                chemin_relatif = os.path.relpath(element_path, start=images_directory)
                chemin_relatif = chemin_relatif.replace('07/', '', 1)
                chemins_images.append(chemin_relatif)
    return chemins_images

images_list = parcourir_dossiers(images_directory)

counter_correct = 0
counter_doesnt_exist = 0
counter_different = 0

for image_name in images_list:
    image_path = os.path.join(images_directory, image_name)
    #print(image_name)  # --> ex: img_741.jpg
    
    try:
        image = face_recognition.load_image_file(image_path)
        
        face_locations = face_recognition.face_locations(image)
        amount = len(face_locations)
        
        img_file_name = '2002/07/' + image_name[:-4]
        #print(img_file_name)
        found_in_text = False
        with open(txt_file_directory, 'r') as fichier:
            lines = fichier.readlines()
            for i, line in enumerate(lines):
                if img_file_name in line:
                    if i + 1 < len(lines):
                        ligne_suivante = lines[i + 1].strip() 
                        if ligne_suivante == str(amount):
                            counter_correct += 1
                        else:
                            counter_different += 1
                            # Draw lines around the face(s)
                            img = Image.fromarray(image, 'RGB')
                            draw = ImageDraw.Draw(img)
                            for face_location in face_locations:
                                draw.rectangle([(face_location[3], face_location[0]), (face_location[1], face_location[2])], outline="red", width=3)        
                            img_np = img.convert("RGB")
                            plt.imshow(img_np)
                            plt.axis('off')  # Masquer les axes
                            plt.show()
                    found_in_text = True
                    break
        
        if not found_in_text:
            counter_doesnt_exist += 1

    except Exception as e:
        print(f"ERROR{image_name}: {e}")

# Affichage des résultats
print(f"counter_correct: {counter_correct}")
print(f"counter_different: {counter_different}")
print(f"counter_doesnt_exist: {counter_doesnt_exist}")

