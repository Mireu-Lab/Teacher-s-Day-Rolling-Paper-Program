# SQL 모듈 불러오기
from carnation import read, write

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class ReadData(BaseModel):
    school = str
    teacher_name = str
    class_number = int
    grade = int

class WriteData(BaseModel):
    school = str
    teacher_name = str
    grade = int
    class_number = int
    number = int
    name = str

@app.get("/")
async def main():
    return {"Docs" : "http://execpro.mireu.xyz/"}

@app.post("/write")
async def write_api(WriteData:WriteData, mamo:str):
    write.school = WriteData.school
    write.teacher_name = WriteData.teacher_name
    write.grade = WriteData.grade
    write.class_number = WriteData.class_number
    write.number = WriteData.number
    write.name = WriteData.name
    return write.write(mamo)

@app.post("/read")
async def read_api(ReadData:ReadData):
    read.school = ReadData.school
    read.teacher_name = ReadData.teacher_name
    read.class_number = ReadData.class_number
    read.grade = ReadData.grade
    return read.read()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)