import sys


def get_sound_info(sound):  # gets the username and license of a given sound
    name = sound.name
    username = sound.username
    license_link = sound.license
    return name, username, license_link


def print_info(sound):
    name, username, license_link = get_sound_info(sound)
    print('Sound name: ' + name)
    print('Uploaded by: ' + username)
    print('License type: ' + license_link + '\n')


def print_credits(sounds):
    print('This soundscape was created thanks to freesound.org and the following sounds: \n')
    for sound in sounds:
        print_info(sound)


def write_credits(sounds):
    sys.stdout = open('credits.txt', 'w')
    print_credits(sounds)
    sys.stdout.close()



