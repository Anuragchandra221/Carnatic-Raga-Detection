import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def create_spectrogram(audio_file_path, output_folder):
    y, sr = librosa.load(audio_file_path)

    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    # plt.figure(figsize=(10, 4))
    # librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
    # plt.colorbar(format='%+2.0f dB')
    # plt.title('Spectrogram')
    # plt.xlabel('Time')
    # plt.ylabel('Frequency')
    # plt.tight_layout()

    base_name = os.path.splitext(os.path.basename(audio_file_path))[0]
    output_image_path = f"{output_folder}/{base_name}_spectrogram.png"

    plt.savefig(output_image_path)
    plt.close()
    os.remove(audio_file_path)
    # print(f"Spectrogram saved as {output_image_path}")

def spectro(input_folder_path):

    path = os.path.abspath(os.getcwd()) + "\\model\\test_raga\\"
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename) 
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print(f"Deleted {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")

    # print(input_folder_path)
    for subfolder in os.listdir(input_folder_path):
        # sub_folder = os.path.join(input_folder_path, subfolder)
        # print("hihi")
        flag = 0
        # for file_name in os.listdir(sub_folder):
        if subfolder.endswith('.wav'):
            # flag = 1
            # break
            audio_file_path = os.path.join(input_folder_path, subfolder)
            # print(audio_file_path)
            create_spectrogram(audio_file_path, os.path.abspath(os.getcwd()) + "\\model\\test_raga\\")
        if(flag==1):
            print(subfolder)