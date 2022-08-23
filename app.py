from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import numpy as np
import json
import requests

from mysql_connect import mysql_connect
import rtvc_main

app = FastAPI()

class UserInput(BaseModel):
    spec: list
    sr: int

@app.get('/')
def index():
    return {"Message": "This is vocoder API for better project"}

@app.get('/inference/')
def inference(userinput: UserInput):
    userinput = userinput.dict()
    spec = np.array(userinput["spec"])
    sr = userinput["sr"]
    print("spec uploaded")
    wav = rtvc_main.inference(spec)

    wav = np.pad(wav, (0, sr), mode="constant")
    wav = list(wav)
    wav_json = json.dumps({
        "wav": wav,
        "sr": sr
    })
    headers = {
        'Content-Type': 'application/json'
    }
    print("requesting preprocessing to encoder . . .")
    response = requests.request("GET", "https://better-encoder.herokuapp.com/preprocess/", headers=headers, data=wav_json)
    wav = response.json()
    print(wav)
    print("connecting to mysql server")
    msq = mysql_connect()
    print("sending to mysql server")
    msq.send_wav(wav)
    print("wav sent to mysql server")

    # return "done"
    # wav = jsonable_encoder("done")
    return JSONResponse(jsonable_encoder("done"))
    # wav = jsonable_encoder(wav.tolist())
    # return JSONResponse(wav)