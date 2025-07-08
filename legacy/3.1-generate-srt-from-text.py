import json
import os
from datetime import timedelta

from config import SUBTITLE_JSON_FILE
from config import SUBTITLE_SRT_FILE




def format_time(seconds):
    '''
    초 단위 시간을 SRT 형식(HH:MM:SS,mmm)으로 변환
    '''

    td = timedelta(seconds=seconds)
    hours = int(td.total_seconds() // 3600)
    minutes = int((td.total_seconds() % 3600) // 60)
    seconds = int(td.total_seconds() % 60)
    milliseconds = int((td.total_seconds() % 1) * 1000)

    return f'{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}'

# print(format_time(3662.567))

## segments(test.json) 불러오기
with open(SUBTITLE_JSON_FILE, 'r', encoding='utf-8') as file:
    segments = json.load(file)

# print(segments[0])
# print(len(segments))

# for i, seg in enumerate(segments, 1):
#     print(i)
#     print(format_time(seg['start']))
#     print(format_time(seg['end']))
#     print(f"{format_time(seg['start'])} --> {format_time(seg['end'])}")
#     print(seg['text'].strip())
#     print(type(seg), end='\n\n')


## srt 파일 작성
with open(SUBTITLE_SRT_FILE, 'w', encoding='utf-8') as file:
    for i, seg in enumerate(segments, 1):
        start = format_time(seg['start'])
        end = format_time(seg['end'])
        text = seg['text'].strip()

        file.write(f'{i}\n')
        file.write(f'{start} --> {end} \n')
        file.write(f'{text}\n\n')
    
print(f'SRT 저장 완료: {SUBTITLE_SRT_FILE}')
