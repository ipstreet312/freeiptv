#! /usr/bin/python3

import requests
import os
import sys
import json
import time


headers={
        "User-Agent": "Equidia/6036 CFNetwork/1220.1 Darwin/20.3.0",
        "Referer": "https://fr.equidia.app/"
}

s = requests.Session()
response = s.get('https://api.equidia.fr/api/public/racing/equidia-mobileapp-ios-1/equidia-live2', headers=headers).json()['primary']
print(response)
