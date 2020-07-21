#!/usr/bin/python3
'''
    This module creates objects of type Label given csv file
'''
import csv
import django
import os
import boto3
import pprint
import json
import urllib.request
from requests import get
from urllib.request import Request, urlopen

os.environ.setdefault("DJANGO_SETTINGS_MODULE","iMagic_v1.settings")
django.setup()
from my_app.models import Image, Label


def label_to_DB():
    '''
        Brings all Image instances to make requests to AWS Rek and create
        objects of type Label
    '''
    with open("./access.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_list = list(csv_reader)
        access_key_id = csv_list[0][0]
        secret_access_key = csv_list[1][0]

    img_formats = ["jpg", "png"]
    all_imgs = Image.objects.all()
    # img_aws_limit = 5242879
    line_count = 0
    for img in all_imgs:
        print(line_count)
        if line_count > 20944:
            url = img.image_url
            if url == '' or 'default-main' in url:
                continue
            print("before: {}".format(url))
            if url.split('.')[-1].split('\n')[0] in img_formats:
                try:
                    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
                    webpage = urlopen(req, timeout=120).read()
                    print(img.image_url)
                    client = boto3.client(
                        'rekognition',
                        aws_access_key_id=access_key_id,
                        aws_secret_access_key=secret_access_key,
                        region_name="us-east-2"
                        )
                
                    #response = client.detect_labels(Image={'Bytes': webpage},MaxLabels=10) /Use this line if it is desired to work with object and scene detection
                    response = client.detect_custom_labels(
                        ProjectVersionArn="arn:aws:rekognition:us-east-2:017784105438:project/manually-labeled-images/version/manually-labeled-images.2020-06-16T13.55.40/1592333741191",
                        Image={'Bytes': webpage},
                        MaxResults=10,
                        MinConfidence=0)
                    for item in response.get('CustomLabels'):
                        l1 = Label(
                            label_name=item.get('Name'),
                            label_confidence=item.get('Confidence'),
                            #instances=json.dumps(item.get('Instances')), /Use this line if it is desired to work with object and scene detection
                            #parents=json.dumps(item.get('Parents')), /Use this line if it is desired to work with object and scene detection
                            image=img
                            )
                        l1.save()
                except Exception as e:
                    print(e)

                
        line_count += 1
            

if __name__ == '__main__':
    label_to_DB()
