import sys

"""This file contains the functions used to list all sounds used in a soundscape along with their respective licenses.
"""


def get_sound_info(sound):
    """Get username and license of a sound
    """
    name = sound.name
    username = sound.username
    license_link = sound.license
    return name, username, license_link


def print_info(sound):
    """Display an individual sound's information
    """
    name, username, license_link = get_sound_info(sound)
    print('Sound name: ' + name)
    print('Uploaded by: ' + username)
    print('License type: ' + license_link + '\n')


def print_credits(sounds):
    """Display sound info of a given array of sounds
    """
    print('This soundscape was created thanks to freesound.org and the following sounds: \n')
    for sound in sounds:
        print_info(sound)


def write_credits(sounds):
    """Write a text file with the credits
    """
    sys.stdout = open('credits.txt', 'w')
    print_credits(sounds)
    sys.stdout.close()



