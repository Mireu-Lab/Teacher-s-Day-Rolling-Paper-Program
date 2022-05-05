import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import json

with open("/Date/info.json", "r") as program_info:
    project_info = program_info.read()

cred = credentials.Certificate(project_info["Firebase"]["Key"])
firebase_admin.initialize_app(cred,{
    'databaseURL' : project_info["Firebase"]["URL"]
})

school = None
teacher_name = None
class_number = None
grade = None

def read():
    global school, teacher_name, grade, class_number
    ret = re.sub('[~!@#$%^&*()_-+{}|:;<>?/}]', '', f"{school}.{grade}.{class_number}.{teacher_name}")
    
    ref = db.reference(ret)
    return ref.get()