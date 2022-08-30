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
