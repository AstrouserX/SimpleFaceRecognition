import cv2
import os
import time
import numpy as np
import codecs, json
import face_recognition
from imutils.video import FPS
from imutils.video import VideoStream


def faces_compare_result(file, path, object, flag, last_name):
   photos_list = [i.split("[")[0] for i in os.listdir(path)]
   print(photos_list.count(file))
   cv2.imwrite(f"{path}/{file}[{photos_list.count(file)}].jpg", object)
   last_name = last_name
   flag == flag
   
   return last_name, flag

directory = "emploee_face_data" # emploee face data in json format

images = np.array(os.listdir(directory))

print(images)

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

vs = VideoStream(src=0,framerate=10).start()
time.sleep(2.0)
fps = FPS().start()

un_name = "undefined"

path_way = "checked_camera_photos" # <path to save checked images>

last_name = None

flag = True

while True:
   try:
      img = vs.read()
      gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      faces = faceCascade.detectMultiScale(
         gray_img, scaleFactor=1.2, minNeighbors=5)
      print(type(faces))

      if type(faces)!=tuple and faces.any():
         face_locations = [faces[0][1], faces[0][2]+faces[0][0], faces[0][3]+faces[0][1], faces[0][0]]
         known_face_locations = [tuple(face_locations)]

         print(known_face_locations)

         image_to_be_matched_encoded = face_recognition.face_encodings(img)[0]

         for image in images:
            obj_text = codecs.open(f"{directory}/{image}", 'r', encoding='utf-8').read()
            b_new = json.loads(obj_text)
            current_image_encoded = np.array(b_new)

            result = face_recognition.compare_faces(
                        [image_to_be_matched_encoded], current_image_encoded)
            
            image = image.split(".")
            
            if result[0] == True and image[0] != last_name:
               last_name, flag = faces_compare_result(image[0], path_way, img, False, None)

               break

         if result[0] != True and flag == True:
            last_name, flag = faces_compare_result(un_name, path_way, img, True, None)

      elif type(faces)==tuple:
         flag = True
         last_name = None

   except Exception as e:
      print(repr(e))
      print("Don't see a face.")
      
   cv2.destroyAllWindows()