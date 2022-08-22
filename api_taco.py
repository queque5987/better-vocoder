import requests
import json
import librosa
import numpy as np

url = "https://better-encoder.herokuapp.com/inference/"
def get_embed():
    wav, sr = librosa.load("19-227-0009.wav")
    wav = wav.tolist()
    wav_json = json.dumps({
        "wav": wav,
        "sr": sr
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=wav_json)
    embed = np.array(response.json())
    return embed