#!/usr/bin/python3
'''
    Populates DB with json file
'''
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","iMagic_v1.settings")
django.setup()
from my_app.models import Course, Label
import json


def populate_DB():
    with open('../../Python_scripts/files_csv/data.json', 'r') as file_read:
        dict_data = json.load(file_read)
        for value in dict_data.values():
            int_var = value.get("class_sku")
            if int_var:
                print(int_var)
                obj_course = Course(
                    class_title = value.get("class_title"),
                    class_sku = int(int_var),
                    class_image = value.get("class_image"),
                    class_url= value.get("class_url"))
                obj_course.save()
                for label in value.get("labels"):
                    try:
                        obj_label = Label.objects.get(label_title=label)
                    except:
                        obj_label = Label(label_title = label)
                        obj_label.save()
                    obj_label.courses.add(obj_course)

if __name__ == '__main__':
    populate_DB()
