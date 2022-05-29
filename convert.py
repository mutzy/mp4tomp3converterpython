from moviepy.editor import *
import os
from pathlib import Path
from flask import Flask, render_template, redirect, request, url_for, session, jsonify
# from flask_session import Session



app = Flask(__name__)

app.debug = "False"
app.env = "Production"

app.secret_key = "991077a6175a2cf43c4771f569ed0b0b361d7d69"

def conversion_algo():

    print(os.getcwd())
    music_folder = os.chdir("/home/bunasiliatechnologies/Videos/new/")
    print("navigating to music mp4 format folder {0}".format(os.getcwd()))
    print("Folder contents :{0}".format(len(os.listdir())))

    try: 
        conversion_folder = "/home/bunasiliatechnologies/Music/converted/new/"
        os.mkdir(conversion_folder)
    except OSError as error: 
        print(error) 


    # iterate over files in
    # that directory
    for mp4file in os.listdir():
        mp4file_to_path = Path(mp4file)
        videoclip = VideoFileClip(mp4file)
        audioclip = videoclip.audio
        size = len(mp4file)
        audioclip.write_audiofile(os.path.join(conversion_folder, "{0}mp3".format(mp4file[:size - 3])))
        print("Done with : {0}".format(mp4file))

    audioclip.close()
    print("closing audioclip")
    videoclip.close()
    print("closing video clip")

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()