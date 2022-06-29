from pydub import AudioSegment
from pydub.playback import play
import time
import random
import database as db
import os
import audio3d

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
        audio_segments_background = audio3d.mono_conv(sorting(generate_audio_segments(path)))
        background = audio3d.low_pass(audio_segments_background[0], -20)
        if len(audio_segments_background) <= 1:
            right_track = background
            left_track = background
            return background, right_track, left_track
        else:
            for i in range(1, len(audio_segments_background)):
                right_track = audio3d.low_pass(background.overlay(audio_segments_background[i]), -10)
                left_track = audio3d.low_pass(background.overlay(audio_segments_background[i]), -10)
                return background, right_track, left_track


def create_foreground(path, background, right_track, left_track, pos):
    """Create the foreground of the soundscape using the corresponding sounds.
    """
    if os.path.exists(path):
        audio_segments_foreground = audio3d.mono_conv(sorting(generate_audio_segments(path)))
        back_duration = len(background)
        dur_sec = background.duration_seconds
        prob = dur_sec/60
        count = 0  # count total foreground sounds
        if len(audio_segments_foreground) <= 3:
            for sound in audio_segments_foreground:
                left_or_right = 0
                position = pos[count]
                middle = (1250/2)  # screen size of the interface
                if position >= middle:
                    left_or_right = 1
                else:
                    left_or_right = 0
                n = round(back_duration % prob)
                if n == 0:
                    n = 1
                for i in range(n):
                    start_index = random.randint(0, back_duration)
                    if left_or_right == 0:
                        left_track = left_track.overlay(audio3d.fading_audios(sound, -20), position=start_index)
                        right_track = right_track.overlay(audio3d.fading_audios(sound, -20), position=start_index)
                    elif left_or_right == 1:
                        left_track = left_track.overlay(audio3d.fading_audios(sound, -20), position=start_index)
                        right_track = right_track.overlay(audio3d.fading_audios(sound, -20), position=start_index)
                    mixed = AudioSegment.from_mono_audiosegments(left_track, right_track)
                count += 1
        elif len(audio_segments_foreground) > 3:
            for sound in audio_segments_foreground:
                while count <= 3:
                    left_or_right = 0
                    position = pos[count]
                    middle = (1250/2)  # screen size of the interface
                    if position >= middle:
                        left_or_right = 1
                    else:
                        left_or_right = 0
                    n = round(back_duration % prob)
                    if n == 0:
                        n = 1
                    for i in range(n):
                        start_index = random.randint(0, back_duration)
                        if left_or_right == 0:
                            left_track = left_track.overlay(audio3d.fading_audios(sound, -20), position=start_index)
                            right_track = right_track.overlay(audio3d.fading_audios(sound, -20), position=start_index)
                        elif left_or_right == 1:
                            left_track = left_track.overlay(audio3d.fading_audios(sound, -20), position=start_index)
                            right_track = right_track.overlay(audio3d.fading_audios(sound, -20), position=start_index)
                        mixed = AudioSegment.from_mono_audiosegments(left_track, right_track)
                    count += 1
                if count > 3:
                    left_or_right = random.randint(0, 1)
                    n = round(back_duration % prob)
                    if n == 0:
                        n = 1
                    for i in range(n):
                        start_index = random.randint(0, back_duration)
                        if left_or_right == 0:
                            left_track = left_track.overlay(audio3d.fading_audios(sound, -20), position=start_index)
                            right_track = right_track.overlay(audio3d.fading_audios(sound, -20),
                                                              position=start_index)
                        elif left_or_right == 1:
                            left_track = left_track.overlay(audio3d.fading_audios(sound, -20), position=start_index)
                            right_track = right_track.overlay(audio3d.fading_audios(sound, -20),
                                                              position=start_index)
                        mixed = AudioSegment.from_mono_audiosegments(left_track, right_track)
    return mixed