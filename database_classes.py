import inspect, sys


"""
This file creates some basic environment instances with some related sounds in order to make certain scenarios more immersive.
"""

class Forest:
    def __init__(self):
        self.sounds = ["chirping", "leaves rustling", "insects", "bird", "wind", "birds"]
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
        self.sounds = ["helicopter", "car horn", "phone ringing", "dog barking", "engines", "sirens", "cars", "wind", "birds chirping"]
        self.background = ["helicopter", "car horn", "phone ringing", "dog barking"]
        self.foreground = ["sirens", "cars", "wind", "birds chirping"]


class Beach:
    def __init__(self):
        self.sounds = ["waves", "birds chirping", "wind", "tropical bird"]
        self.background = ["waves", "birds chirping", "wind"]
        self.foreground = ["tropical bird", "wind", "waves"]


class Airport:
    def __init__(self):
        self.sounds = ["helicopters",  "airplanes", "engines", "planes", "cars", "sirens", "megaphone", "people talking", "rolling suitcases"]
        self.background = ["helicopters",  "airplanes", "engines", "planes"]
        self.foreground = ["cars", "sirens", "megaphone", "people talking", "rolling suitcases"]


class Hospital:
    def __init__(self):
        self.sounds = ["sirens", "people screaming", "people crying", "hospital", "phone ringing", "megaphone", "people talking", "wheelchair", "sneezes", "cough"]
        self.background = ["sirens", "people screaming", "people crying", "hospital"]
        self.foreground = ["phone ringing", "megaphone", "people talking", "wheelchair", "sneezes", "cough"]


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


