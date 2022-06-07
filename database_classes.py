import freesound
import os
import inspect, sys

FREESOUND_API_KEY = 'e2tYlnLzVgrRfWUnlXmOHwK7aDICqeNw8fujVubQ'
FILES_DIR = 'files classes'  # Place where to store the downloaded files. Will be relative to the current folder.
DATAFRAME_FILENAME = 'dataframe.csv'  # File where we'll store the metadata of our sounds collection
FREESOUND_STORE_METADATA_FIELDS = ['id', 'name', 'username', 'previews', 'license',
                                   'tags']  # Freesound metadata properties to store

freesound_client = freesound.FreesoundClient()
freesound_client.set_token(FREESOUND_API_KEY)
if not os.path.exists(FILES_DIR): os.mkdir(FILES_DIR)


class Forest:
    def __init__(self):
        self.sounds = ["chirping", "leaves rustling", "insects", "bird", "wind", "crickets", "birds"]
        self.background = ["bird", "leaves rustling", "insects"]
        self.foreground = ["chirping", "wind", "crickets", "birds"]


class Rainforest:
    def __init__(self):
        self.sounds = ["birds chirping", "insects, buzzing", "cicadas", "frogs", "tropical bird", "wind", "monkey"]
        self.background = ["birds chirping", "insects", "buzzing", "cicadas", "frogs"]
        self.foreground = ["tropical bird", "wind", "monkey"]


class Desert:
    def __init__(self):
        self.sounds = ["wind", "eagle", "snake", "sand"]
        self.background = ["wind", "sand"]
        self.foreground = ["eagle", "snake"]


class City:
    def __init__(self):
        self.sounds = ["cars", "people talking", "sirens", "engines"]
        self.background = ["helicopter", "insects, buzzing", "car, horn", "phone, ringing", "dog, barking"]
        self.foreground = ["sirens", "cars", "wind", "birds chirping"]


class Beach:
    def __init__(self):
        self.sounds = ["waves", "wind", "cars", "children, screaming", ]
        self.background = ["waves", "birds chirping", "wind", "people talking", "music"]
        self.foreground = ["tropical bird", "wind", "waves"]


class Airport:
    def __init__(self):
        self.sounds = ["engines", "planes", "whistle", "people talking", ]
        self.background = ["cars", "birds chirping", "helicopters", "rolling suitcases"]
        self.foreground = ["cars", "sirens", "megaphone"]


class Hospital:
    def __init__(self):
        self.sounds = ["people talking", "cars", "sirens", "megaphone", "crying babies"]
        self.background = ["sirens", "people screaming", "people crying", "wheelchair", "sneezes", "cough"]
        self.foreground = ["phone, ringing", "sirens", "people talking"]


class Stadium:
    def __init__(self):
        self.sounds = ["people screaming", "whistle", "people talking", ""]
        self.background = ["music", "whistle", "birds chirping", "megaphone"]
        self.foreground = ["bounced ball", "popcorn", "sirens"]


def get_classes():
    class_names = []
    class_objects = []
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            class_names.append(name.lower())
            class_objects.append(obj)
    return class_names, class_objects



