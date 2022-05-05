import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import re

try:
    app = firebase_admin.get_app()
except ValueError as e:
    cred = credentials.Certificate("Data/carnation-mireu-xyz-firebase-adminsdk-p3fgl-a1df3d92e0.json")
    firebase_admin.initialize_app(cred, {'databaseURL':'https://carnation-mireu-xyz-default-rtdb.firebaseio.com/'})

def firebase_read(school, teacher_name, grade, class_number):
    ret =  re.sub('[-=.#/?:$}]', '', f"{school}.{grade}.{str(class_number)}.{teacher_name}")
    
    ref = db.reference(ret)
    return ref.get()