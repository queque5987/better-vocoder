# from this import d
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse, FileResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import json
import requests

from mysql_connect import mysql_connect
import rtvc_main

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    spec: list
    sr: int

@app.get('/')
def index():
    return FileResponse("index.html")

@app.post('/inference/')
def inference(userinput: UserInput):
    """
    @request
        mel spectrogram data to generate {list}
            converted {tensor} mel spectrogram to {list}, and its sample_rate {int}
    @response
        generated wav {list}
            use librosa or any library to turn this to listenable wav file.

    **This method returns voice file inferenced by mel spectrogram**
    """
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
    response = requests.request("POST", "https://better-encoder.herokuapp.com/preprocess/", headers=headers, data=wav_json)
    wav = response.json()
    wav = eval(wav)
    wav = wav['wav']
    
    print("connecting to mysql server . . . ")
    msq = mysql_connect()
    print("getting index from table . . . ")
    idx = msq.get_wav_idx()
    idx += 1
    print("idx : {}".format(idx))
    del msq
    print("connecting to mysql server . . . ")
    msqa = mysql_connect()
    print("sending to mysql server . . . ")
    msqa.send_wav(idx, wav)
    print("wav sent to mysql server . . . ")
    
    wav_json = json.dumps({
        "wav": wav,
        "sr": sr
    })
    return JSONResponse(wav_json)