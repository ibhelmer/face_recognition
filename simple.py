# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 23:03:03 2020

@author: Ib Helmer Nielsen
"""
import requests
from PIL import Image
import os
import APIConfig as api

image_path = os.path.join('D:\Dropbox\GitHub\Face_recognition\me_without_glas.jpg')
image_data = open(image_path, "rb")

my_key, api_url = api.config();

headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': my_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion'
}

response = requests.post(api_url, params=params, headers=headers, data=image_data)
response.raise_for_status()
faces = response.json()
print(faces)