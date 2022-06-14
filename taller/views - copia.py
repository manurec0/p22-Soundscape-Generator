# importing the necessary libraries
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import text_synthesis as ts
import database_classes as db_classes
import database as db
import interface as interface
import licenses
import audio
import os
import shutil



def initial(request):
    if request.method == 'GET':
        return render(request, 'initial.html')

    if request.method == 'POST':
        text = request.POST["text"]
        x1 = request.POST["x1"]
        y1 = request.POST["y1"]
        x2 = request.POST["x2"]
        y2 = request.POST["y2"]
        x3 = request.POST["x3"]
        y3 = request.POST["y3"]
        print(text, " ", x1, "\n")
        print(text, " ", y1, "\n")

        dict = {
            'text': text,
            'x1': x1,
            'y1': y1,
            'x2': x2,
            'y2': y2,
            'x3': x3,
            'y3': y3
        }

        keywords, synonyms = ts.query(text)
        class_names, class_objects = db_classes.get_classes()

        filter = 'channels:1 type:wav tag:field-recording'
        filterbackground = 'channels:2 type:wav tag:field-recording tag:background'
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
                # queries = db.generate_queries(sounds, filter, num_results)
                # db.generate_previews(sounds, filter, num_results, path)
                # background_sounds
                back_sounds = instance.background
                if not os.path.exists(path + '/' + 'background'): os.mkdir(path + '/' + 'background')
                db.generate_previews(back_sounds, filterbackground, num_results, path + '/' + 'background')
                # foreground_sounds
                fore_sounds = instance.foreground
                if not os.path.exists(path + '/' + 'foreground'): os.mkdir(path + '/' + 'foreground')
                db.generate_previews(fore_sounds, filter, num_results, path + '/' + 'foreground')
            elif item.lower() not in class_names:
                if not os.path.exists(path + '/' + 'background'):
                    os.mkdir(path + '/' + 'background')
                    sound_list.append(item)
                    list = [item]
                    db.generate_previews(list, filterbackground, num_results, path + '/' + 'background')
                    if len(os.listdir(path + '/' + 'background')) == 0:
                        filter_failsafe = 'channels:2 type:wav tag:background'
                        db.generate_previews(list, filter_failsafe, num_results, path + '/' + 'background')
                sound_list.append(item)
                list = [item]
                if not os.path.exists(path + '/' + 'foreground'):
                    os.mkdir(path + '/' + 'foreground')
                db.generate_previews(list, filter, num_results, path + '/' + 'foreground')
        dir = audio.setpath()
        background = audio.create_background(format(dir + '/' + 'background'))
        mixed = audio.create_foreground(format(dir + '/' + 'foreground'), background)
        os.chdir(format(dir))
        mixed.export("mixed.wav", format='wav')
        queries = db.generate_queries(sound_list, filter, num_results)
        licenses.print_credits(queries)
        return render(request, 'initial.html', dict)
