data face found here : http://vis-www.cs.umass.edu/fddb/
library found here : https://face-recognition.readthedocs.io/en/latest/face_recognition.html
4 different codes:
- face_recognition for 1 image : for one image return how many face(s), draw rectangle on the face(s) and return also the top right point and the bottom left point that create the rectangle
- face_recognition with rectangle on face : for all the subset of the dataset 2002/07/19/big/ return the images with the rectangle(s) on face(s)
- comparison of faces found with face_recognition and the dataset : for all the subset of the dataset 2002/07/19/big/ it returns counter_correct:50, counter_different:17 and counter_doesnt_exist:13
- draw rectangles when there is not the good amount of face : for all the subset /2002/07/ it returns counter_correct: 601, counter_different: 207, counter_doesnt_exist: 126and draw rectangle when face recognition and the dataset don't have the same amount of face(s)
