# SQL 모듈 불러오기
from carnation import read, write

from fastapi import FastAPI, UploadFile, File
import uvicorn

app = FastAPI()

@app.get("/")
def main():
    return {"Docs" : "http://execpro.mireu.xyz/"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)