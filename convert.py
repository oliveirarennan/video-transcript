import os

toMp3Command = 'ffmpeg -i "./data/etrue1.m4v" -acodec libmp3lame -ab 128k "./data/output/etrue1.mp3"'
toWavCommand = 'ffmpeg -i "./data/output/etrue1.mp3" "./data/output/etrue1.wav"'


def convert_video_to_audio():
    print('Converting video to audio MP3...')
    # os.system(toMp3Command)
    print('Converting MP3 to  WAV...')
    # os.system(toWavCommand)
    print('Done converting!')
