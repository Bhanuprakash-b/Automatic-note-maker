import moviepy.editor
from os import path
from pydub import AudioSegment
from tkinter.filedialog import *
video=askopenfilename()
video=moviepy.editor.VideoFileClip(video)
audio=video.audio
audio.write_audiofile("Aud.wav")
print("completed")                                                                        
