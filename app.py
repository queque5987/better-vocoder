from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import numpy as np

import rtvc_main

app = FastAPI()

class UserInput(BaseModel):
    spec: list

@app.get('/')
def index():
    return {"Message": "This is vocoder API for better project"}

@app.get('/inference/')
def inference(userinput: UserInput):
    userinput = userinput.dict()
    spec = np.array(userinput["spec"])
    print("spec uploaded")
    wav = rtvc_main.inference(spec)
    print(wav)
    wav = jsonable_encoder(wav.tolist())
    return JSONResponse(wav)