from pathlib import Path
import api_taco
from vocoder import inference as vocoder
import soundfile as sf
import numpy as np

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
    vocoder.load_model(args.voc_model_fpath)
    generated_wav = vocoder.infer_waveform(spec)
    return generated_wav

# if __name__ == "__main__":
    # sample_rate = 16000
    # generated_wav = vocoder.infer_waveform(spec)