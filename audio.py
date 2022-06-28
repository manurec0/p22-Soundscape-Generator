from pydub import AudioSegment
from pydub.playback import play
import time
import random
import database as db
import os

prob = 15

"""This file contains the functions to mix all sounds and create a single .wav file with the soundscape.
"""


def setpath():
    """Set working directory to the correct path.
    """
    cwd = os.getcwd()
    path = format(cwd) + '/' + db.FILES_DIR
    return path


def generate_audio_segments(path):
    """Generate working audio segments from the given preview files of the sounds.
    """
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
    """Basic list sorting.
    """
    lst2 = sorted(lst, key=len)
    lst2 = lst2[::-1]
    return lst2


def create_background(path):
    """Create the background of the soundscape using the corresponding sounds.
    """
    if os.path.exists(path):
        audio_segments_background = sorting(generate_audio_segments(path))
        background = audio_segments_background[0]
        for i in range(1, len(audio_segments_background)):
            background = background.overlay(audio_segments_background[i])
    return background


def create_foreground(path, background):
    """Create the foreground of the soundscape using the corresponding sounds.
    """
    if os.path.exists(path):
        audio_segments_foreground = sorting(generate_audio_segments(path))
        mixed = background
        back_duration = len(background)
        for sound in audio_segments_foreground:
            n = back_duration % prob
            for i in range(n):
                start_index = random.randint(0, back_duration)
                pan_random = random.uniform(-1, 1)
                mixed = mixed.overlay(sound.pan(pan_random), position=start_index)

    return mixed