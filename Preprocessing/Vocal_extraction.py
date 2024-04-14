# from spleeter.separator import Separator
# import spleeter 
import soundfile as sf
import librosa

def vocal_extract(input_path, output_path):
    # seperator = spleeter.separator.Separator("spleeter:2stems")
    # vocals = seperator.separate_to_file(input_path, output_path)

    # Load audio file
    y, sr = librosa.load(input_path)

    # Apply HPSS algorithm to separate vocals from accompaniment
    y_harmonic, y_percussive = librosa.effects.hpss(y)

    # Invert the separation to reconstruct the vocal component
    vocals = y_harmonic - y_percussive

    # Write the extracted vocals to a new audio file
    # librosa.output.write_wav(output_path, vocals, sr)
    sf.write(output_path, vocals, 48000, 'PCM_24')
    # librosa.output.write_wav("accompaniment.wav", y_accompaniment, sr)
