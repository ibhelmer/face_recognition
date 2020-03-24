# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:59:58 2020

@author: Ib Helmer Nielsen
"""

my_key =  #"ENTER YOUR KEY HERE" #DSFace API
api_url = 'https://pbaptiface.cognitiveservices.azure.com/face/v1.0/detect'  #'https://eastus2.api.cognitive.microsoft.com/face/v1.0/detect'


def config():
    print("Call Config")
    return my_key, api_url