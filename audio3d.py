from pydub import AudioSegment
import random


def mono_conv(list):
    for p in range(0, len(list)):
        list[p] = list[p].set_channels(1)
    return list


def fading_audios(sound, gain):
    gain = random.randint(gain, 0)
    sound = sound.fade(to_gain=gain, start=0, end=len(sound))
    return sound


def get_background(background_list):
    cont = 0
    for sound in range(0, len(background_list)):
        if len(background_list[sound]) > cont:
            cont = len(background_list[sound])
            background = background_list[sound]
        else:
            continue
    return background


def low_pass(sound, value):
    if sound.dBFS > value:
        sound = sound.apply_gain(value-sound.dBFS)
    return sound