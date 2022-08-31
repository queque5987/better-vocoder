from pathlib import Path
from better_encoder.encoder.inference import is_loaded
from vocoder import inference as vocoder

import requests
import json
import librosa
import numpy as np
import soundfile as sf


def inference(spec):
    if not vocoder.is_loaded:
        print("loading vocoder . . . ")
        vocoder.load_model("/")
    print("inferring waveform . . . ")
    generated_wav = vocoder.infer_waveform(spec)
    print("wav generated . . . ")
    return generated_wav
