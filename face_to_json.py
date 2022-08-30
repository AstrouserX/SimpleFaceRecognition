import numpy as np
import codecs, json 
import face_recognition
import numpy as np
import os


images = np.array(os.listdir('emploee_photos'))

directory = "emploee_face_data"

for image in images:
   current_image = face_recognition.load_image_file("emploee_photos/" + image)
   current_image_encoded = face_recognition.face_encodings(current_image)[0]
   json_name = image.split('.')[0]
   file_path = f"{directory}/{json_name}.json"
   with open(file_path, "w") as file:
      b = current_image_encoded.tolist() # nested lists with same data, indices
      json.dump(b, codecs.open(file_path, 'w', encoding='utf-8'), 
               separators=(',', ':'), 
               sort_keys=True, 
               indent=4) ### this saves the array in .json format