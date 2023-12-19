import subprocess

import whisper

from convert import convert_video_to_audio

model = whisper.load_model("medium")

# convert_video_to_audio()

path_to_audio = "./data/output/etrue1.mp3"

print("Transcribing...")

# transcript = model.transcribe(path_to_audio)

subprocess.run(
    [
        "whisper",
        "--language", "pt",
        "--word_timestamps", "True",
        "--model", "medium",
        "--output_dir", f"output-{'medium'}",
        path_to_audio
    ]
)

# with (open("./data/output/etrue1.txt", "w")) as f:
#     f.write(transcript["text"])
#     print('Done!')

# print('File save at ./data/output/etrue1.txt')
