import os
import sys
import subprocess
import requests
import ssl
import random
import string
import json

from flask import jsonify
from flask import Flask
from flask import request
from flask import send_file
import traceback


from app_utils import download
from app_utils import generate_random_filename
from app_utils import clean_me
from app_utils import clean_all
from app_utils import create_directory
from app_utils import get_model_bin


from zipfile import ZipFile

from spleeter.audio.adapter import get_default_audio_adapter
from spleeter.separator import Separator

from uuid import uuid4
from pyunpack import Archive


from os.path import basename

import tarfile

try:  # Python 3.5+
    from http import HTTPStatus
except ImportError:
    try:  # Python 3
        from http import client as HTTPStatus
    except ImportError:  # Python 2
        import httplib as HTTPStatus


app = Flask(__name__)


def load_audio(audio_file):
    waveform, rate = audio_loader.load(audio_file)
    return waveform, rate


def save_audio(path, instrument, data, rate):
    audio_loader.save(os.path.join(path, f'{instrument}.wav'), data, rate, 'wav', '128k')


@app.route("/process", methods=["POST"])
def process():

    input_path = generate_random_filename(upload_directory, "mp3")
    folder_random = str(uuid4())

    output_path = '/src/output/' + folder_random
    create_directory(output_path)
    
    zip_output_path = generate_random_filename(upload_directory, "zip")


    try:
        url = request.json["url"]
        #2stems or 4stems or 5stems
        nb_stems = request.json["nb_stems"]
        
        download(url, input_path)

        separator = separators[int(nb_stems)]

        waveform, rate = load_audio(input_path)

        result = separator.separate(waveform)

        zip = ZipFile(zip_output_path + '.zip', 'w')
        
        for instrument, data in result.items():
            save_audio(output_path, instrument, data, rate)
            for (root,dirs,files) in os.walk(output_path):
                with ZipFile(zip_output_path, 'w') as zip:
                    for file in files:
                        print(file)
                        zip.write(output_path + '/' + file, basename(file))

        callback = send_file(zip_output_path, mimetype='application/zip')


        return callback, 200


    except:
        traceback.print_exc()
        return {'message': 'input error'}, 400


    finally:
        clean_all([
            input_path,
            output_path,
            zip_output_path
            ])


if __name__ == '__main__':
    global separator
    global model_directory
    global audio_loader
    global upload_directory
    global separators

    upload_directory = "/src/upload/"
    create_directory(upload_directory)

    model_directory = "/src/pretrained_models/"
    create_directory(model_directory)
    

    model_url_prefix = 'http://pretrained-models.auth-18b62333a540498882ff446ab602528b.storage.gra.cloud.ovh.net/sound/spleeter/'

    separators = dict()

    for model in ["2stems", "4stems", "5stems"]:
        separators[int(model[0])] = Separator('spleeter:' + model)
        download(model_url_prefix + model + '.tar.gz', model_directory + model + '.tar.gz')
        create_directory(model_directory + model + '/')
        
        cmd = 'tar zxvf ' + model_directory + model + '.tar.gz' + ' -C ' + model_directory + model
        os.system(cmd)

    audio_loader = get_default_audio_adapter()

    port = 5000
    host = '0.0.0.0'

    app.run(host=host, port=port, threaded=False)

