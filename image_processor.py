# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:10:09 2023

@author: Karsyn
"""
from tensorflow.keras.models import load_model
import numpy as np
import face_recognition
import cv2

gender_model = load_model('models/gender_model3')
age_model = load_model('models/age_model2')
#both_model = load_model('models/both_models')
EXTRA_PIXELS = 50
def analyze_image(img):
        copy = img.copy()
        face_locations = face_recognition.face_locations(copy)
        for face in face_locations:
                # crop and resize image to pass into model
                cropped = copy[face[0]-EXTRA_PIXELS:face[2]+EXTRA_PIXELS, face[3]-EXTRA_PIXELS:face[1]+EXTRA_PIXELS]
                resized = cv2.resize(cropped, (256,256))
                
                input_img = np.expand_dims(resized, axis=0)
                # normalize the pixel values to [0, 1]
                input_img = input_img / 255.0
                
                # Make a prediction
                gender_prediction = gender_model.predict(input_img)
                age_prediction = age_model.predict(input_img)
                #prediction = both_model.predict(input_img)
                predicted_age = str(round(age_prediction[0][0], 0))
                predicted_gender = 'Male' if gender_prediction[0][0] > 0.5 else 'Female'
                
                
                # Draw rectangle and age/gender annotations
                cv2.rectangle(copy, (face[3]-EXTRA_PIXELS, face[0]-EXTRA_PIXELS),(face[1]+EXTRA_PIXELS, face[2]+EXTRA_PIXELS), (0,255,0), 2)
                
                # Only detect a single face
                return copy, predicted_age, predicted_gender
        
        # This means no image was detected
        return None, None, None