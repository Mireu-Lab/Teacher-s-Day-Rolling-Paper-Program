# SQL 모듈 불러오기
from carnation import write, read

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class ReadData(BaseModel):
    school : str
    teacher_name : str
    class_number : int
    grade : int

class WriteData(BaseModel):
    school : str
    teacher_name : str
    grade : int
    class_number : int
    number : int
    name : str
    memo : str

@app.get("/")
async def main():
    return {"Docs" : None}

@app.post("/write")
async def write_api(WriteData:WriteData):
    return write.firebase_write(
        WriteData.school,
        WriteData.teacher_name,
        WriteData.grade,
        WriteData.class_number,
        WriteData.number,
        WriteData.name,
        WriteData.memo
    )

@app.post("/read")
async def read_api(ReadData:ReadData):
    return read.firebase_read(
        ReadData.school,
        ReadData.teacher_name,
        ReadData.class_number,
        ReadData.grade
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)