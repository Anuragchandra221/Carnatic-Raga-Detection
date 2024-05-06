from pydub import AudioSegment

def convert_to_wav(input_file, output_path):
    try:
        sound = AudioSegment.from_file(input_file)
        sound.export(output_path, format="wav")
        print("Conversion successful!")
    except Exception as e:
        print(f"Error: {e}")