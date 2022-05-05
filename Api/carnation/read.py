import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import re

cred = credentials.Certificate("Data/carnation-mireu-xyz-firebase-adminsdk-p3fgl-a1df3d92e0.json")
firebase_admin.initialize_app(cred)

school = None
teacher_name = None
class_number = None
grade = None

def read():
    global school, teacher_name, grade, class_number
    ret = re.sub('[~!@#$%^&*()_-+{}|:;<>?/}]', '', f"{school}.{grade}.{class_number}.{teacher_name}")
    
    ref = db.reference(ret)
    return ref.get()