from flask import Flask, render_template, request, send_file
import os
import librosa
import soundfile as sf
from TTS.api import TTS

app = Flask(__name__)

os.makedirs("uploads", exist_ok=True)
os.makedirs("output", exist_ok=True)
os.makedirs("models", exist_ok=True)

os.environ["TTS_HOME"] = os.path.abspath("models")

tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=False)

def preprocess_audio(input_path, output_path):
    """Convert to mono, normalize, and resample to 22050Hz for best TTS results."""
    y, sr = librosa.load(input_path, sr=22050, mono=True)
    y = librosa.util.normalize(y)
    sf.write(output_path, y, 22050)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    audio_file = request.files["audio"]
    text = request.form["text"]

    raw_ref_path = os.path.join("uploads", audio_file.filename)
    audio_file.save(raw_ref_path)

    clean_ref_path = os.path.join("uploads", "clean_ref.wav")
    preprocess_audio(raw_ref_path, clean_ref_path)

    # Output path
    output_path = os.path.join("output", "voice_output.wav")

    tts.tts_to_file(
        text=text,
        speaker_wav=clean_ref_path,  
        language="en",
        file_path=output_path,
        speed=1.15  
    )

    return send_file(output_path, mimetype="audio/wav", as_attachment=True, download_name="synthesized.wav")

if __name__ == "__main__":
    app.run(debug=True)
