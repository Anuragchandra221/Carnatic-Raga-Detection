from flask import Flask, render_template, request
from werkzeug.utils import secure_filename 
from Preprocessing.convert_to_wav import convert_to_wav
from Preprocessing.Vocal_extraction import vocal_extract
import os
import pathlib
from Preprocessing.splitting_to_chunks import split_audio
from Preprocessing.create_spectrogram import spectro
from model.raga import predict_raga
from download_yt import download_audio

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict", methods = ['POST', 'GET'])
def predict():
    if(request.method=="POST"):
        audio = request.files['audiofile']
        yt = request.form['anurag']
        print(yt, 'yt')
        if(audio):
            filename = secure_filename(audio.filename)
            file_path = os.path.join("uploads", filename)
            audio.save(file_path)

            wav_filename = os.path.splitext(filename)[0] + '.wav'
            # wav_file_path = os.path.join("uploads", wav_filename)

            # convert_to_wav(filename, wav_file_path)
            # os.remove(file_path)
            path = os.path.abspath(os.getcwd())
            path += "\\uploads\\" + filename
            # wav_file_path = os.path.abspath(os.getcwd()) + "\\uploads\\" + wav_filename
            # vocal_extract(path, wav_file_path)
            split_audio(path, segment_duration_ms=5000)
            path = os.path.abspath(os.getcwd()) + "\\uploads\\split_audios\\"
            spectro(path)
            path = os.path.abspath(os.getcwd()) + "\\model\\test_raga\\"
            most_common = predict_raga(path)

            return render_template("predict.html", raga=most_common)
        else:
            download_audio(yt)
            convert_to_wav('uploads/audio.mp3', 'uploads/audio.wav')
            # path = "\\uploads\\audio.wav"
            split_audio('uploads/audio.wav', segment_duration_ms=5000)
            path = os.path.abspath(os.getcwd()) + "\\uploads\\split_audios\\"
            spectro(path)
            path = os.path.abspath(os.getcwd()) + "\\model\\test_raga\\"
            most_common = predict_raga(path)
 
            return render_template("predict.html", raga=most_common)

    return render_template("predict.html")

if __name__=="__main__":
    app.run(debug=True)