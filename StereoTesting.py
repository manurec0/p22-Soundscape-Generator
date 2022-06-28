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


#background
wave1 = AudioSegment.from_file("SoundsStereoTest/Wave1.wav")
children_playing = AudioSegment.from_file("SoundsStereoTest/Children_playing.wav")
wind = AudioSegment.from_file("SoundsStereoTest/Wind.wav")

#foreground
wave2 = AudioSegment.from_file("SoundsStereoTest/wave2.wav")
people_talking = AudioSegment.from_file("SoundsStereoTest/people_talking.wav")
seagulls = AudioSegment.from_file("SoundsStereoTest/seagulls.wav")

#storing in lists
background_list = [children_playing, wave1, wind]
foreground_list = [wave2, people_talking, seagulls]

#mono conversion
background_list = mono_conv(background_list)
foreground_list = mono_conv(foreground_list)

#get_background
background = get_background(background_list)

right_track = AudioSegment.silent(duration=len(background))
left_track = AudioSegment.silent(duration=len(background))

#background
for i in range(0, len(background_list)):
    background_list[i] = low_pass(background_list[i], -35)
    right_track = right_track.overlay(background_list[i], loop=True)
    left_track = right_track.overlay(background_list[i], loop=True)


#foreground
for i in range(0, len(foreground_list)):
    foreground_list[i] = low_pass(foreground_list[i], -20)
    foreground_list[i] = fading_audios(foreground_list[i], -6)#fade_audios
    left_or_right = random.randint(0, 1)
    position1 = random.randint(0, len(background))
    position2 = random.randint(0, len(background))
    times = int(len(background)/(1000*60))
    if left_or_right == 0:
        left_track = left_track.overlay(foreground_list[i], position=position1, times=2*times)
        right_track = right_track.overlay(foreground_list[i], position=position2, times=times)
    elif left_or_right == 1:
        left_track = left_track.overlay(foreground_list[i], position=position1, times=times)
        right_track = right_track.overlay(foreground_list[i], position=position2, times=2*times)

#audio synthesis
stereo_test = AudioSegment.from_mono_audiosegments(left_track, right_track)
stereo_test.export("SoundsStereoTest/StereoTest.wav", format="wav")
