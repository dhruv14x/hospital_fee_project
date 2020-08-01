# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 07:01:37 2020

@author: dhruv
"""

import requests
#from data_input import data_in
data_in = [36.0, 30.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0]
URL = 'http://127.0.0.1:5000/predict'
headers  = {"Content-Type":"application/json"}
data = {"input": data_in}

r = requests.get(URL, headers=headers, json=data)
r.json()
