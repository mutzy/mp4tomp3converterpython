from moviepy.editor import *
import os
from pathlib import Path


print(os.getcwd())
music_folder = os.chdir("/home/bunasiliatechnologies/Videos/")
print("navigating to music mp4 format folder {0}".format(os.getcwd()))
print("Folder contents :{0}".format(len(os.listdir())))

try: 
    conversion_folder = "/home/bunasiliatechnologies/Music/converted/"
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