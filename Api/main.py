# SQL 모듈 불러오기
from carnation import read, write

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class SetData(BaseModel):
    school = str
    teacher_name = str
    class_number = int
    grade = int

@app.get("/")
async def main():
    return {"Docs" : "http://execpro.mireu.xyz/"}

@app.post("/write")
async def write():
    pass

@app.post("/read")
async def read():
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)