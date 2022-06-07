from pydub import AudioSegment
from pydub.playback import play
import time
import random
import database as db
import os

prob = 70

# background = ["chirping", "leaves rustling"]
# filter = 'channels:1 type:wav tag:field-recording'
# num_results=1

def setpath():
    cwd = os.getcwd()
    path = format(cwd) + '/files database'
    return path


# db.generate_previews(background, filter, num_results, path)


def generate_audio_segments(path):
    os.chdir(path)
    file_list = os.listdir(path)
    audio_segments = []
    for file in file_list:
        if file.endswith('.ogg'):
            audio = AudioSegment.from_ogg(file)
            audio_segments.append(audio)
        else:
            pass
    return audio_segments


def sorting(lst):
    lst2 = sorted(lst, key=len)
    lst2 = lst2[::-1]
    return lst2


def create_background(path):
    if os.path.exists(path):
        audio_segments_background = sorting(generate_audio_segments(path))
        background = audio_segments_background[0]
        for i in range(1, len(audio_segments_background)):
            background = background.overlay(audio_segments_background[i])
        backDuration = len(background)
    return background

def create_foreground(path, background):
    if os.path.exists(path):
        audio_segments_foreground = sorting(generate_audio_segments(path))
        mixed = background
        backDuration = len(background)
        for sound in audio_segments_foreground:
            n = backDuration % prob
            for i in range(n):
                startIndex = random.randint(0, backDuration)
                panRandom = random.uniform(-1, 1)
                mixed = mixed.overlay(sound.pan(panRandom), position=startIndex)

    return mixed

