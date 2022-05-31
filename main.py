import text_synthesis as ts
import database_classes as db_classes
import database as db
import interface as interface

text = interface.run()
keywords, synonyms = ts.query(text)
class_names, class_objects = db_classes.get_classes()

for item in keywords:
    if item.lower() in class_names:
        index = class_names.index(item.lower())
        class_name = class_names[index].capitalize()
        obj = class_objects[index]
        class_ = getattr(db_classes, class_name)
        instance = class_()
        sounds = instance.sounds
        queries = db.generate_queries(sounds)
        previews = db.generate_previews(queries)


