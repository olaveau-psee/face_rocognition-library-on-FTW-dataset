import face_recognition
import os

# repertory path
images_directory = '/home/olivia/Documents/FTW_facedetection/originalPics/2002/07/19/big/'
txt_file_directory = '/home/olivia/Documents/FTW_facedetection//FDDB-folds/alltogether.txt'


images_list = os.listdir(images_directory)
counter_correct = 0
counter_doesnt_exist = 0
counter_different = 0
for image_name in images_list:
    image_path = os.path.join(images_directory, image_name)
    #print(image_name) --> ex: img_741.jpg
    try:
        image = face_recognition.load_image_file(image_path)
        
        # Face detection
        face_locations = face_recognition.face_locations(image)
        amount = len(face_locations)
        
        # Comparison with txtfile
        img_file_name = '2002/07/19/big/'+image_name[:-4]
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
                            counter_different+=1
                    found_in_text = True
                    break
        
        if not found_in_text:
            counter_doesnt_exist+=1

    except Exception as e:
        print(f"ERROR{image_name}: {e}")

print(f"counter_correct:{counter_correct}")
print(f"counter_different:{counter_different}")
print(f"counter_doesnt_exist:{counter_doesnt_exist}")