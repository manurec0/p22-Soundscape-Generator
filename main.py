import text_synthesis as ts
import database_classes as db_classes

keywords, synonyms = ts.query()

class_names, class_objects = db_classes.get_classes()

for item in keywords:
    if item.lower() in class_names:
        index = class_names.index(item.lower())
        class_name = class_names[index].capitalize()
        obj = class_objects[index]
        class_ = getattr(db_classes, class_name)
        instance = class_()


