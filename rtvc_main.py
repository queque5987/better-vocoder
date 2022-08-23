from pathlib import Path
from vocoder import inference as vocoder

import requests
import json
import librosa
import numpy as np
import soundfile as sf



class rtvc_args():
    def __init__(self):
        self.voc_model_fpath = Path("saved_models/vocoder")
        self.cpu = True
        self.seed = None
    def pop(self, idx):
        if idx == "cpu":
            return self.cpu

def inference(spec):
    args = rtvc_args()
    print("loading vocoder")
    vocoder.load_model(args.voc_model_fpath)
    print("inferring waveform")
    generated_wav = vocoder.infer_waveform(spec)
    print("wav generated")
    return generated_wav

if __name__ == "__main__":

    url = {
        "encoder-inference": "https://better-encoder.herokuapp.com/inference/",
        "encoder-preprocess": "https://better-encoder.herokuapp.com/preprocess/",
        "synthesizer": "https://better-synthesizer.herokuapp.com/inference/",
        "vocoder": "https://better-vocoder.herokuapp.com/inference/"
    }
    text = "It's a rocket."
    wav, sr = librosa.load("19-227-0009.wav")
    wav = wav.tolist()
    wav_json = json.dumps({
        "wav": wav,
        "sr": sr
    })
    headers = {
        'Content-Type': 'application/json'
    }
    # print("requesting embed to encoder . . .")
    response = requests.request("GET", url["encoder-inference"], headers=headers, data=wav_json)
    embed = response.json()
    # print(embed)
    # print(type(embed))
    embed_json = json.dumps({
        "embed": embed,
        "text": text
    })
    print("requesting spec to synthesizer . . .")
    response = requests.request("GET", url["synthesizer"], headers=headers, data=embed_json)
    # spec = np.array(response.json())
    # wav = inference(spec)
    spec = response.json()

    print(len(spec))
    print(len(spec[0]))
    
    spec_json = json.dumps({
        "spec": spec,
        "sr": sr
    })
    print("requesting wav to vocoder . . .")
    # response = requests.request("GET", url["vocoder"], headers=headers, data=spec_json)
    requests.request("GET", url["vocoder"], headers=headers, data=spec_json)
    # wav = np.array(response.json())


    # wav = np.pad(wav, (0, sr), mode="constant")
    # wav = list(wav)
    # wav_json2 = json.dumps({
    #     "wav": wav,
    #     "sr": sr
    # })
    # print("requesting preprocessing to encoder . . .")
    # response = requests.request("GET", url["encoder-preprocess"], headers=headers, data=wav_json2)
    # wav = np.array(response.json())

    # sf.write("testing_deploied_server.wav", wav.astype(np.float32), 16000)
    print("done")