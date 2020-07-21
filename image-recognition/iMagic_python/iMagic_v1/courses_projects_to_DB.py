#!/usr/bin/python3
"""
    This module create instances of Course and Project from csv file
    to populate our database
"""


import csv
import django
import json
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","iMagic_v1.settings")
django.setup()
from my_app.models import Course, Project


def course_project_to_DB():
    '''
        Creates objects of type Course and Project
    '''
    line_count = 0
    with open('../../csv_files/files_csv/holberton-skillshare-top-classes.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            #if line_count == 100:
                #break
            if line_count == 0:
                pass
            else:
                if check_labels(row[1]):
                    line_count_2 = 0
                    c1 = Course(class_title=row[0], class_url=row[2], class_sku=row[1], class_image=row[3])
                    c1.save()
                    flag = False
                    flag1 = False
                    with open('../../csv_files/files_csv/holberton-skillshare-top-classes-projects.csv') as csv_file_2:
                        csv_reader_2 = csv.reader(csv_file_2, delimiter=',')
                        for row_2 in csv_reader_2:
                            if line_count_2 == 0:
                                pass
                            else:
                                if row[1] == row_2[0]:
                                    flag = True
                                    flag1 = True
                                    project_id = row_2[-2].split('/')[-1]
                                    project_title = row_2[1]
                                    project_url = row_2[-2]
                                    print('*'*10)
                                    print(project_id)
                                    print(project_url)
                                    p1 = Project(project_id=project_id, project_title=project_title, project_url=project_url, course=c1)
                                    p1.save()
                                else:
                                    flag = False
                            if flag == False and flag1 == True:
                                break
                            line_count_2 += 1
            line_count += 1
            print(line_count)

def check_labels(sku):
    """This function checks if the labels in the model appear in the course labels"""

    hand_labels_list = ["Manga", "Graphic", "Design", "Comics", "Sketch", "Animation", "Digital Illustration", "Blender", "Motion Graphics",
    "Adobe Photoshop", "Adobe Illustrator", "Painting", "Sketching", "Animation 3D", "Comic Character", "Surface Design", "Logo Design",
    "Pen Drawing", "Oil Painting", "3D Design", "3D Character", "Ink Illustration", "Pencil Drawing", "Ink Drawing", "Character Animation",
    "Watercolor Painting", "Cinema", "Digital Drawing", "Vektor", "Figure Drawing", "3D Rendering", "Acrylic Painting", "After Effects", "Pattern Design",
    "4D", "Watercolors", "Animation 2D", "Drawing", "3D Graphics"]
    with open('../../csv_files/files_csv/skillshare_labels.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                pass
            if sku == row[0]:
                list_label = row[-1].split("+")
                for label in list_label:
                    if label in hand_labels_list:
                        return True
                return False
            line_count += 1
        return False
                        



if __name__ == '__main__':
    course_project_to_DB()
