from appium_mainprogram import main as appium_main
from subprocess import Popen
from fastapi import FastAPI

app = FastAPI()

Popen(["appium"])

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/run-appium")
async def root():
    appium_main()
    return {"message": "Hello World"}