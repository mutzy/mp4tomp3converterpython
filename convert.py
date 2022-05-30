from ast import Store
from moviepy.editor import *
import os
from pathlib import Path
from flask import Flask, render_template, redirect, request, url_for, session, jsonify
# from flask_session import Session
# import pyrebase
import urllib

from werkzeug.utils import secure_filename

app = Flask(__name__)

app.debug = "False"
app.env = "Production"

app.secret_key = "991077a6175a2cf43c4771f569ed0b0b361d7d69"


# Your web app's Firebase configuration

# For Firebase JS SDK v7.20.0 and later, measurementId is optional

# config={
#     'apiKey': "AIzaSyANCLEgJCdeGEpMauDaujxl4FKCXUT23Bo",
#     'authDomain': "mp4convertr.firebaseapp.com",
#     'projectId': "mp4convertr",
#     'storageBucket': "mp4convertr.appspot.com",
#     'databaseURL': "https://mp4convertr-default-rtdb.firebaseio.com",
#     'messagingSenderId': "496466736940",
#     'appId': "1:496466736940:web:7980b3f7012fb36c79de89",
#     'measurementId': "G-P8VR69SGTZ"
#   }
# firebase=pyrebase.initialize_app(config)

# #define storage
# storage=firebase.storage()


ALLOWED_EXTENSIONS = set(['mp4'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def conversion_algo():

#     print(os.getcwd())
    # music_folder = os.chdir("/home/bunasiliatechnologies/Videos/new/")
    # print("navigating to music mp4 format folder {0}".format(os.getcwd()))
    # print("Folder contents :{0}".format(len(os.listdir())))

    # try: 
    #     conversion_folder = "/home/bunasiliatechnologies/Music/converted/new/"
    #     os.mkdir(conversion_folder)
    # except OSError as error: 
    #     print(error) 


    # iterate over files in
    # that directory
    # for mp4file in os.listdir():
    #     mp4file_to_path = Path(mp4file)
    #     videoclip = VideoFileClip(mp4file)
    #     audioclip = videoclip.audio
    #     size = len(mp4file)
    #     audioclip.write_audiofile(os.path.join(conversion_folder, "{0}mp3".format(mp4file[:size - 3])))
    #     print("Done with : {0}".format(mp4file))

    # audioclip.close()
    # print("closing audioclip")
    # videoclip.close()
    # print("closing video clip")

@app.route("/",methods=['GET'])
def index():
    print(os.getcwd())
    return render_template('index.html')

@app.route("/conversion", methods=['POST'])
def convert():
    if request.method == 'POST':
        if 'files[]' not in request.files:
            # flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
   
                # videoclip = VideoFileClip(f)
                # audioclip = videoclip.audio
                # audioclip.write_audiofile()
                # file.save(os.path.join(, filename))
        return redirect(url_for('index'))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()