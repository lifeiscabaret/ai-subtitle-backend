from moviepy import VideoFileClip
from datetime import timedelta,datetime
from config import (
    VIDEO_FILE, AUDIO_FILE,
    SUBTITLE_DIR
)
import whisper
import os


def format_time(seconds):
    td = timedelta(seconds=seconds)
    hours = int(td.total_seconds() // 3600)
    minutes = int((td.total_seconds() % 3600) // 60)
    seconds = int(td.total_seconds() % 60)
    milliseconds = int((td.total_seconds() % 1) * 1000)
    return f'{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}'


def generate_srt_from_video(input_video_path, output_audio_path,subtitle_dir):

    # ## 1. 영상 -> 오디오 ###################################

    # print('1. 영상 → 오디오 추출')

    # ## 객체 생성
    # video = VideoFileClip(input_video_path)

    # ## 비디오에서 오디오 추출
    # video.audio.write_audiofile(output_audio_path, fps=16000, nbytes=2, codec='pcm_s16le')

    # ## 리소스 해제
    # video.close()

    ## 2. 오디오 -> segments ######################################
    print('\n\n2. 오디오 -> Whisper로 텍스트 변환(segments 포함)')

    ## 모델 생성
    model = whisper.load_model("small")

    ## 텍스트 변환
    # result = model.transcribe(output_audio_path)
    result = model.transcribe(input_video_path)

    ## segments만 저장
    segments = result['segments']

    ## 3. segments -> srt 저장 #########################################
    print('\n\n3. segments -> srt 저장')

    ## srt 파일: 고유한 파일명 지정
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    subtitle_srt_path = os.path.join(subtitle_dir, f'subtitle_{timestamp}.srt')


    with open(subtitle_srt_path, 'w', encoding='utf-8') as f:
        for i, seg in enumerate(segments, 1):
            start = format_time(seg['start'])
            end = format_time(seg['end'])
            text = seg['text'].strip()

        f.write(f'{i}\n')
        f.write(f'{start}--> {end}\n')
        f.write(f'{text}\n\n')
    print(f'4. [SRT 생성] 완료 -> {subtitle_srt_path}')
    return subtitle_srt_path



# 함수 호출 ==================================================
if __name__ == '__main__':
    print('AUDIO_FILE >> ', AUDIO_FILE)
    print('VIDEO_FILE >> ', VIDEO_FILE)
    print('SUBTITLE_SRT_FILE >> ', SUBTITLE_DIR)
generate_srt_from_video(VIDEO_FILE, AUDIO_FILE,SUBTITLE_DIR)