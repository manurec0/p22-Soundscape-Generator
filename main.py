import text_synthesis as ts
import database_classes as db_classes
import database as db
import interface as interface
import Audio
import licenses
import os
import shutil

text = interface.run()
keywords, synonyms = ts.query(text)
class_names, class_objects = db_classes.get_classes()

filter = 'channels:1 type:wav tag:field-recording'
filterBackground = 'channels:2 type:wav tag:field-recording tag:background'
num_results = 1
path = db.FILES_DIR

for filename in os.listdir(path):
    file_path = os.path.join(path, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

for item in synonyms:

    if item.lower() in class_names:
        index = class_names.index(item.lower())
        class_name = class_names[index].capitalize()
        obj = class_objects[index]
        class_ = getattr(db_classes, class_name)
        instance = class_()
        sounds = instance.sounds
        queries = db.generate_queries(sounds, filter, num_results)
        db.generate_previews(sounds, filter, num_results, path)
        # background_sounds
        back_sounds = instance.background
        if not os.path.exists(path + '/' + 'background'): os.mkdir(path + '/' + 'background')
        db.generate_previews(back_sounds, filterBackground, num_results, path + '/' + 'background')
        # foreground_sounds
        fore_sounds = instance.foreground
        if not os.path.exists(path + '/' + 'foreground'): os.mkdir(path + '/' + 'foreground')
        db.generate_previews(fore_sounds, filter, num_results, path + '/' + 'foreground')
        path = Audio.setpath()
        audio_segments_all = Audio.sorting(Audio.generate_audio_segments(path))
        background = Audio.create_background(path + '/' + 'background')
        mixed = Audio.create_foreground(path + '/' + 'foreground', background)
        path = Audio.setpath()
        mixed.export("mixed.wav", format='wav')

    #elif item.lower() not in class_names:

     #   path = db.FILES_DIR
      #  if not os.path.exists(path + '/' + 'nonDBsounds'): os.mkdir(path + '/' + 'nonDBsounds')
       # db.sounds_notDatabase(item.lower(), path)
