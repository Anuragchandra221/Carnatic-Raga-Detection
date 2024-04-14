import os
from pydub import AudioSegment

def split_audio(input_path, segment_duration_ms=5000):
    audio = AudioSegment.from_file(input_path)

    num_segments = len(audio) // segment_duration_ms

    for i in range(num_segments):
        start_time = i * segment_duration_ms
        end_time = (i + 1) * segment_duration_ms
        segment = audio[start_time:end_time]

        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_file_path = os.path.abspath(os.getcwd()) + "\\uploads\\split_audios\\" + f"{base_name}{i+1}.wav"

        segment.export(output_file_path, format="wav")

        print(f"Segment {i + 1} exported to {output_file_path}")

    os.remove(input_path)


