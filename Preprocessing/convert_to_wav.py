from pydub import AudioSegment

def convert_to_wav(input_file, output_path):
    # input_path.replace("\\", "/")
    # output_path.replace("\\", "/")
    print('input path', input_file)
    sound = AudioSegment.from_mp3(f"uploads/{input_file}")
    # audio.export(output_path, format="wav")