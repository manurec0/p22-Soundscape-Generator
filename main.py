import text_synthesis as ts
import database_classes as db_classes
import database as db
import licenses
import audio
import os
import shutil


def main(text, pos):

    keywords, synonyms = ts.query(text)
    class_names, class_objects = db_classes.get_classes()

    filter = 'type:wav tag:field-recording'
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

    sound_list = []
    for item in keywords:
        if item.lower() in class_names:
            index = class_names.index(item.lower())
            class_name = class_names[index].capitalize()
            obj = class_objects[index]
            class_ = getattr(db_classes, class_name)
            instance = class_()
            sounds = instance.sounds
            sound_list += sounds
            # background_sounds
            back_sounds = instance.background
            if not os.path.exists(path + '/' + 'background'): os.mkdir(path + '/' + 'background')
            db.generate_previews(back_sounds, filterBackground, num_results, path + '/' + 'background')
            # foreground_sounds
            fore_sounds = instance.foreground
            if not os.path.exists(path + '/' + 'foreground'): os.mkdir(path + '/' + 'foreground')
            db.generate_previews(fore_sounds, filter, num_results, path + '/' + 'foreground')
        elif item.lower() not in class_names:
            if not os.path.exists(path + '/' + 'background'):
                os.mkdir(path + '/' + 'background')
                sound_list.append(item)
                list = [item]
                db.generate_previews(list, filterBackground, num_results, path + '/' + 'background')
                if len(os. listdir(path + '/' + 'background')) == 0:
                    filter_failsafe = 'channels:2 type:wav tag:background'
                    db.generate_previews(list, filter_failsafe, num_results, path + '/' + 'background')
            sound_list.append(item)
            list = [item]
            if not os.path.exists(path + '/' + 'foreground'): os.mkdir(path + '/' + 'foreground')
            db.generate_previews(list, filter, num_results, path + '/' + 'foreground')

    dir = audio.setpath()
    try:
        background, right_track, left_track = audio.create_background(format(dir + '/' + 'background'))
        mixed = audio.create_foreground(format(dir + '/' + 'foreground'), background, right_track, left_track, pos)
        os.chdir(format(dir))
        mixed.export("mixed.wav", format='wav')

        queries = db.generate_queries(sound_list, filter, num_results)
        licenses.print_credits(queries)
    except IndexError:
        print("There was an error fetching your sounds! Try changing your wording or being more descriptive.")
