import os


# print(__file__)
# c:\course_video\16_ai\ai-model-development\backend\config.py

# print(os.path.dirname(__file__))
# c:\course_video\16_ai\ai-model-development\backend

## 기본 디렉토리
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# print('BASE_DIR >>', BASE_DIR)
# c:\course_video\16_ai\ai-model-development\backend

## 폴더 경로 
VIDEO_DIR = os.path.join(BASE_DIR, 'source', 'video')
AUDIO_DIR = os.path.join(BASE_DIR, 'source', 'audio')
SUBTITLE_DIR = os.path.join(BASE_DIR, 'source', 'subtitle')

## 파일명 
file_name = 'test'
VIDEO_FILE = os.path.join(VIDEO_DIR, f'{file_name}.mp4')
AUDIO_FILE = os.path.join(AUDIO_DIR, f'{file_name}.wav')
SUBTITLE_TEXT_FILE = os.path.join(SUBTITLE_DIR,f'{file_name}.txt')
SUBTITLE_JSON_FILE = os.path.join(SUBTITLE_DIR,f'{file_name}.json')
SUBTITLE_SRT_FILE = os.path.join(SUBTITLE_DIR,f'{file_name}.srt')

print(VIDEO_DIR)
print(VIDEO_FILE)