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
**{tensor} must be converted into {list}*
### Response JSON
    wav @type {list}      
**return array buffer of user's voice*   
**in python, convert wav{list} to {ndarray} to use*   
~**due to timeout error, I have sent wav{list} dirently to DB instead of response*~

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

-----
Better-API (vocoder)
=============

### Better-API는 사용자의 목소리로 문장을 읽어주는 소리 파일을 만들어 냅니다.   
    1.인코더는 사용자의 목소리와 임베딩을 생성하여 신세사이저로 전달합니다.   
    2.신세사이저는 사용자 목소리 임베딩과 문장을 통해 멜스펙트로그램을 생성하여 보코더로 전달합니다.   
    3.보코더는 멜스펙트로그램을 통해 소리 파일을 생성합니다.   
       
*인코더는 Speaker embedding 모델을 사용합니다.*   
*신세사이저는 TACOTRON2 모델을 사용합니다. 용량 문제 때문에 better-synthesizer-w 서버에 업로드되어 있습니다.*   
*보코더는 waveRNN 모델을 사용합니다.*   
    
## 서버 API 링크   
https://better-vocoder.herokuapp.com/

## 엔드포인트 링크   
https://better-vocoder.herokuapp.com/inference/

### Request JSON
    spec @type {list}
    sr @type {int}
**멜스펙트로그램을 전달받습니다.*   
**{tensor}타입의 멜스펙트로그램을 {list}로 변환하고 요청해야 합니다.*

### Response JSON
    wav @type {list}      
**사용자의 목소리 파일을 리스트 형태로 반환합니다.*   
**파이선에서 사용 시, {list}타입을 {ndarray}타입으로 변환하여 사용해야 합니다.*   
~**접속시간 제한으로 인하여 만들어진 wav {list}를 DB에 전송하였습니다.*~

* * *
# 참고
## Real-Time-Voice-Cloning
https://github.com/CorentinJ/Real-Time-Voice-Cloning

## FastAPI   
FastAPI를 통해 개발되었습니다.   
source : https://fastapi.tiangolo.com/   

## Heroku
배포를 위해 Heroku를 사용하였습니다.    
librosa를 설치하기 위해서 Heroku에 해당 빌드팩을 추가하였습니다. (https://github.com/heroku/heroku-buildpack-apt)   
https://dashboard.heroku.com/

## requirements.txt
### For deployment
    fastapi
    pydantic
    uvicorn
    favicon
    gunicorn
### For Voice clonning   
    -f https://download.pytorch.org/whl/torch_stable.html
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
**첫 번째 줄을 추가하여 cpu에 해당하는 torch를 설치합니다.*
