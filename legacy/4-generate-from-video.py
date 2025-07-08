import os
import json
from datetime import timedelta
import whisper
from moviepy import VideoFileClip

from config import (
    VIDEO_FILE, AUDIO_FILE,
    SUBTITLE_DIR, SUBTITLE_TEXT_FILE,
    SUBTITLE_JSON_FILE, SUBTITLE_SRT_FILE
)


def format_time(seconds):
    td = timedelta(seconds=seconds)
    hours = int(td.total_seconds() // 3600)
    minutes = int((td.total_seconds() % 3600) // 60)
    seconds = int(td.total_seconds() % 60)
    milliseconds = int((td.total_seconds() % 1) * 1000)
    return f'{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}'


def generate_srt_from_video():
    print("1. [영상 → 오디오 추출] 시작")
    video = VideoFileClip(VIDEO_FILE)
    video.audio.write_audiofile(AUDIO_FILE, fps=16000, nbytes=2, codec='pcm_s16le')
    video.close()
    print("1. [영상 → 오디오 추출] 완료")

    print("2. [Whisper 모델 로드 및 텍스트 추출]")
    model = whisper.load_model("small")
    result = model.transcribe(AUDIO_FILE)

    os.makedirs(SUBTITLE_DIR, exist_ok=True)

    print("3. [텍스트 저장]")
    with open(SUBTITLE_TEXT_FILE, 'w', encoding='utf-8') as f:
        f.write(result['text'])

    print("4. [segments 저장]")
    with open(SUBTITLE_JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(result['segments'], f, ensure_ascii=False, indent=2)

    print("5. [SRT 파일 저장 시작]")
    segments = result['segments']
    with open(SUBTITLE_SRT_FILE, 'w', encoding='utf-8') as f:
        for i, seg in enumerate(segments, 1):
            start = format_time(seg['start'])
            end = format_time(seg['end'])
            text = seg['text'].strip()

            f.write(f"{i}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{text}\n\n")

    print(f"SRT 저장 완료: {SUBTITLE_SRT_FILE}")


# 실행
generate_srt_from_video()