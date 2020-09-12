from io import BytesIO
import kaldiserve as ks
import glob, time, os, subprocess
from flask import Flask, request, redirect, url_for, render_template, jsonify, send_from_directory, send_file
from werkzeug.utils import secure_filename
from scipy.io import wavfile

ALLOWED_EXTENSIONS = set(['flac', 'mp3', 'wav'])
app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def transcribe(decoder: ks.Decoder, wav_stream: bytes):
    with ks.start_decoding(decoder):
        # decode the audio
        decoder.decode_wav_audio(wav_stream)
        # get the transcripts
        alts = decoder.get_decoded_results(1, False, False)
    return alts

# model specification
model_spec = ks.parse_model_specs("../resources/model-spec.toml")[0]
# create decoder queue
decoder_queue = ks.DecoderQueue(model_spec)
    
@app.route('/')
def hello():
    return 'ASR SERVER READY...'
@app.route('/upload', methods=['POST'])
def upload():
    #load input files
    file = request.files['file']
    if file and allowed_file(file.filename):
        # standard werkzeug method for making sure a file isn't malicious
        filename = secure_filename(file.filename)
        print(filename)
        with open(filename, "rb") as f:
            audio_bytes = BytesIO(f.read()).getvalue()
        with ks.acquire_decoder(decoder_queue) as decoder:
            alts = transcribe(decoder, audio_bytes)
            print(alts)
    return jsonify(alts[0].transcript,alts[0].confidence)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8090, threaded=True)
    
