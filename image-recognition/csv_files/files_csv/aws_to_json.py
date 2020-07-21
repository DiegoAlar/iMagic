#!/usr/bin/python3
import csv
import os
import boto3
import urllib.request
from requests import get
from urllib.request import Request, urlopen
import pprint
import json

with open("../access.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_list = list(csv_reader)
    access_key_id = csv_list[0][0]
    secret_access_key = csv_list[1][0]

DB_dict = {}
img_formats = ["jpg", "png"]


line_count = 0
with open('holberton-skillshare-top-classes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        id_class = row[1]
        name_class = row[0]
        class_url = row[2]
        class_image = row[3]
        if line_count == 0:
            pass
        else:
            labels_list = []
            dict_class = {}
            line_count_2 = 0
            flag = False
            flag1 = False
            with open('holberton-skillshare-top-classes-projects.csv') as csv_file_2:
                csv_reader_2 = csv.reader(csv_file_2, delimiter=',')
                for row_2 in csv_file_2:
                    if line_count_2 == 0:
                        pass
                    else:
                        
                        
                        if  id_class == row_2.split(',')[0]:
                            flag = True
                            flag1 = True
                            
                            splitted = row_2.split(',')[3].split('.')[-1].split('\n')[0]
                            
                            if splitted in img_formats:
                                try:
                                    req = Request(row_2.split(',')[3], headers={'User-Agent': 'XYZ/3.0'})
                                    webpage = urlopen(req, timeout=10).read()
                                    client = boto3.client('rekognition', aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key, region_name = "us-west-2")
                                    response = client.detect_labels(Image={'Bytes': webpage},MaxLabels=10)
                                    
                                    count = 0
                                    for item in response.get('Labels'):
                                        if count <= 5 and (item.get('Name') not in labels_list):
                                            labels_list.append(item.get('Name'))
                                    dict_class['class_title'] = name_class
                                    dict_class['class_sku'] = id_class
                                    dict_class['labels'] = labels_list
                                    dict_class['class_url'] = class_url 
                                    dict_class['class_image'] = class_image         

                                except:
                                    pass
                        else:
                            flag = False
                    if flag == False and flag1 == True:
                        break
                            
                    line_count_2 += 1
                DB_dict[id_class] = dict_class
                
        line_count += 1
        print(line_count)
        with open('data.json', 'w') as outfile:
            json.dump(DB_dict, outfile)
