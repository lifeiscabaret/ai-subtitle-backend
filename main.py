from fastapi import FastAPI, UploadFile, File
import os
import whisper
from datetime import datetime,timedelta
from fastapi.middleware.cors import CORSMiddleware


## 디렉토리 생성 ###############################
## 동영상이 저장되는 폴더: uploads
## SRT 파일이 저장되는 폴더: output
UPLOAD_DIR = './uploads'
OUTPUT_DIR = './output'

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

## Whisper 모델 로드 ##################################
model = whisper.load_model('small')

## FastAPI app 생성 
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 또는 정확히 ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def index():
    return '환영합니다.'

## 요청 URL: /create_subtitle_video
## 요청 method: post

@app.post('/create_subtitled_video')
# def create_subtitled_video(file): ## 함수에 파라미터만 넣어준 형태, 업로드 할 수 있는 형태 x
async def create_subtitled_video(file: UploadFile = File(...) ): #업로드 가능 형태, +import 추가 ## File(...) 빼고 실행해볼것 
    print('\n=== 비디오 처리 시작 ===')

    ## video 파일명 지정
    ## /uploads/temp_video_20250707_1720.mp4

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    temp_video_path = os.path.join(UPLOAD_DIR,f'temp_video_{timestamp}.mp4')

    ## 업로드 영상 저장
    contents = await file.read()
    ## with문 사용하여 쓰기 작업(a,w,x): wb
    ## 파일 경로 및 파일명: temp_video_path
    with open(temp_video_path, 'wb') as file:
        file.write(contents)
    print('Whisper로 자막 추출 시작')
    result = model.transcribe(temp_video_path)

    segments = result['segments']
    

    ## srt 파일: 파일명 지정
    srt_filename = f'subtitle_{timestamp}.srt'
    srt_path = os.path.join(OUTPUT_DIR, srt_filename)

    ## srt 파일 생성
    ## with문 사용: 쓰기 작업
    with open(srt_path, 'w', encoding='utf-8') as f:
        for i, seg in enumerate(segments, 1):
            start = format_time(seg['start'])
            end = format_time(seg['end'])
            text = seg['text'].strip()

            f.write(f'{i}\n')
            f.write(f'{start}--> {end}\n')
            f.write(f'{text}\n\n')
    return {
    "srt": [
        {
            "index": i,
            "start": format_time(seg['start']),
            "end": format_time(seg['end']),
            "text": seg['text'].strip()
        } for i, seg in enumerate(segments, 1)
    ]
}


## 시간 포맷 변환 함수 ###############################
def format_time(seconds):   
    '''
     초 단위 시간을 SRT형식으로 변환
    '''
    td = timedelta(seconds=seconds)
    hours = int(td.total_seconds() // 3600)
    minutes = int((td.total_seconds() % 3600) // 60)
    seconds = int(td.total_seconds() % 60)
    milliseconds = int((td.total_seconds() % 1) * 1000)
    return f'{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}'

