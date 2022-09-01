Better-API (vocoder)
=============
|Name               |Link                                                |input                             |output                     |
|:------------------|:---------------------------------------------------|:---------------------------------|--------------------------:|
|*voice-cloning     |https://github.com/queque5987/better-voice-cloning  |wav/wample_rate/<br>embedding/text|speech sound               |
|encoder            |https://github.com/queque5987/better-encoder        |wav/sample_rate                   |embedding                  |
|synthesizer        |https://github.com/queque5987/better-synthesizer    |embedding/text                    |mel-spectrogram            |
|synthesizer-model  |https://github.com/queque5987/better-synthesizer-w  |parameters in synthesizer         |mel-spectrogram per batch  |
|vocoder            |https://github.com/queque5987/better-vocoder        |mel-spectrogram                   |speech sound               | 

**voice-cloning simply pass requests for all APIs*

### Better-API generates a voice that cloning user's voice from a text.
    1.encoder recieves a user voice and gives an embedding to synthesizer.
    2.synthesizer recieves an embedding and a text to generate speech and gives mel spectrogram to vocoder.   
    3.vocoder recieves a mel spectrogram and gives generated wav file.   
       
*Encoder speaker embedding Model*   
*Synthesizer uses TACOTRON2 Model; it is on better-synthesizer-w API*   
*Vocoder uses waveRNN Model*   
    
## available on
https://better-vocoder.herokuapp.com/
## to inference, send request on
https://better-vocoder.herokuapp.com/inference/
### Request JSON
    spec @type {list}
    sr @type {int}
**receives Mel spectrogram to generate voice*   
**{ndarray} must be converted into {list}*
### Response JSON
    wav @type {list}      
**return user's embedding*   
**convert wav{list} to {ndarray} to use*   
**due to timeout error, I have sent wav{list} dirently to DB instead of response*

* * *
# used libraries
## Real-Time-Voice-Cloning
https://github.com/CorentinJ/Real-Time-Voice-Cloning

## FastAPI   
developed with FastAPI   
to install librosa : https://github.com/heroku/heroku-buildpack-apt   
source : https://fastapi.tiangolo.com/   

## Heroku
deployed with FastAPI   
https://dashboard.heroku.com/

## requirements.txt
### For deployment
    fastapi
    pydantic
    uvicorn
    favicon
    gunicorn
### For Voice clonning-f https://download.pytorch.org/whl/torch_stable.html
    torch==1.12.1+cpu
    fastapi
    pydantic
    numpy
    uvicorn
    favicon
    gunicorn
    librosa
    scipy
    Unidecode
    pymysql
**first line enableds install torch for cpu when deploying server to heroku*
