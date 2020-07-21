#!/usr/bin/python3
"""
    This module create instances of Image from csv file
    to populate our database
"""


import csv
import django
import json
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","iMagic_v1.settings")
django.setup()
from my_app.models import Course, Project, Image


def imgs_to_DB():
    '''
        Creates objects of type Image
    '''
    line_count = 0
    with open('../../csv_files/files_csv/holberton-skillshare-top-classes-projects.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if line_count == 0:
                pass
            else:
                try:
                    if row[-1] != '' and 'default-main' not in row[-1]:
                        p_obj = Project.objects.get(project_id=int(row[-2].split('/')[-1]))
                        img = Image(project=p_obj, image_url=row[-1])
                        img.save()
                except:
                    pass
            line_count += 1
            print(line_count)


if __name__ == '__main__':
    imgs_to_DB()
