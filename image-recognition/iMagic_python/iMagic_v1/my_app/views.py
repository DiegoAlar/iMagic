from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from elasticsearch import TransportError
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3
import json
import csv
import os
from my_app.models import Course, Label, Image, Project
from django.conf import settings


def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json') 

def get_course_titles(request, label_name):
    '''
        Method that makes a query to DB given a string (to be parsed) 
        Parameters:
            request: HttpRequest Object
            label_name (string): string given by the front-end. Concatenation of labels
        Return:
            json with all courses given label_name string
    '''
    if request.method == 'GET':
        label_list = label_name.split(',')
        courses_dict = {}
        for label in label_list:
            for i in Label.objects.raw(
                '''SELECT my_app_label.id, my_app_label.label_name, my_app_image.project_id, my_app_project.course_id 
                FROM my_app_label 
                INNER JOIN my_app_image 
                ON my_app_label.image_id=my_app_image.id 
                INNER JOIN my_app_project 
                ON my_app_image.project_id=my_app_project.project_id 
                WHERE my_app_label.label_name="{}"'''.format(label)):
                course = Course.objects.get(class_sku=i.course_id)
                courses_dict[i.course_id] = {
                    'class_title': course.class_title,
                    'class_url': course.class_url,
                    'class_image': course.class_image  
                }
        response = json.dumps(courses_dict)
        # try:
        #     label_obj = Label.objects.get(label_title=label_name)

        #     course_dic = {}
        #     for obj in label_obj.courses.all():
        #         inter_dic = {'class_image':  obj.class_image, 'class_url': obj.class_url, 'class_title': obj.class_title}
        #         course_dic[obj.class_sku] = inter_dic
            
        #     response = json.dumps(course_dic)
        

        # except:
        #     response = json.dumps([{'Error': 'No title for such label'}])
    return HttpResponse(response, content_type='text/json') 

def get_course_titles_es(request, label_name=None):
    '''
        Method that receives labels concatenated in string and make a resquest to AWS ElasticSearch
        to search courses with thoses labels inside the concatenated string 
        Parameters:
            request: HttpRequest Object
            label_name (string): string given by the front-end. Concatenation of labels
        Return:
            json with all courses given the ES query
    '''
    host = 'search-courses-4sagicofakcbjwqetzec5p7gs4.us-east-2.es.amazonaws.com' # For example, my-test-domain.us-east-1.es.amazonaws.com
    region = 'us-east-2'
    service = 'es'
    
    if label_name is None:
        response = json.dumps([{'Error': 'No Courses for that image, try uploading a different one!'}])
        return HttpResponse(response, content_type='text/json') 
    
    with open(os.path.join(settings.BASE_DIR, 'access.csv')) as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_list = list(csv_reader)
        access_key_id = csv_list[0][0]
        secret_access_key = csv_list[1][0]
    awsauth = AWS4Auth(access_key_id, secret_access_key, region, service)
    es = Elasticsearch(
        hosts = [{'host': host, 'port': 443}],
        http_auth = awsauth,
        use_ssl = True,
        verify_certs = True,
        connection_class = RequestsHttpConnection
        )
    data = {
        "size": 100,
        "query": {
            "multi_match": {
            "query": label_name.replace(',', ' '),
            }
        }
    }
    
    es_response = es.search(data)
    list_dicts = []
    list_titles = []

    for res in es_response['hits']['hits']:
        a_dict = res.get('_source')
        course = {}
        if a_dict.get('course') not in list_titles:
            course['class_title'] = a_dict.get('course')
            course['class_url'] = a_dict.get('class_url')
            course['class_image'] = a_dict.get('class_image')
            list_dicts.append(course)
        list_titles.append(a_dict.get('course'))

    response = json.dumps(list_dicts)
    
    return HttpResponse(response, content_type='text/json') 

def get_all_projects_es(request):
    '''
        Method that give as response all projects. 
        Parameters:
            request: HttpRequest Object
        Return:
            json with all projects given the ES query
    '''
    host = 'search-courses-4sagicofakcbjwqetzec5p7gs4.us-east-2.es.amazonaws.com' # For example, my-test-domain.us-east-1.es.amazonaws.com
    region = 'us-east-2'
    service = 'es'
    
    with open(os.path.join(settings.BASE_DIR, 'access.csv')) as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_list = list(csv_reader)
        access_key_id = csv_list[0][0]
        secret_access_key = csv_list[1][0]
    awsauth = AWS4Auth(access_key_id, secret_access_key, region, service)
    es = Elasticsearch(
        hosts = [{'host': host, 'port': 443}],
        http_auth = awsauth,
        use_ssl = True,
        verify_certs = True,
        connection_class = RequestsHttpConnection
        )
    data = {
        'size' : 1000,
        'query': {
            'match_all' : {}
       }
    }
    es_response = es.search(data)
    list_dicts = []

    for res in es_response['hits']['hits']:
        a_dict = res.get('_source')
        course = {}
        course['class_title'] = a_dict.get('course')
        course['class_url'] = a_dict.get('class_url')
        course['image_labels'] = a_dict.get('image_labels')
        course['image_url'] = a_dict.get('image_url')
        course['project_title'] = a_dict.get('project_title')
        course['project_url'] = a_dict.get('project_url')


        list_dicts.append(course)

    response = json.dumps(list_dicts)
    
    return HttpResponse(response, content_type='text/json') 

def get_project_by_id_es(request, project_id=None):
    '''
        Method that returns a project given project_id. 
        Parameters:
            project_id: id of the project
            request: HttpRequest Object
        Return:
            json with all projects given the ES query
    '''
    host = 'search-courses-4sagicofakcbjwqetzec5p7gs4.us-east-2.es.amazonaws.com' # For example, my-test-domain.us-east-1.es.amazonaws.com
    region = 'us-east-2'
    service = 'es'
    
    with open(os.path.join(settings.BASE_DIR, 'access.csv')) as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_list = list(csv_reader)
        access_key_id = csv_list[0][0]
        secret_access_key = csv_list[1][0]
    awsauth = AWS4Auth(access_key_id, secret_access_key, region, service)
    es = Elasticsearch(
        hosts = [{'host': host, 'port': 443}],
        http_auth = awsauth,
        use_ssl = True,
        verify_certs = True,
        connection_class = RequestsHttpConnection
        )
    data = {
        'query': {
            'match': {
                'project_id': project_id
            }
       }
    }
    es_response = es.search(data)
    list_dicts = []

    for res in es_response['hits']['hits']:
        a_dict = res.get('_source')
        course = {}
        course['class_title'] = a_dict.get('course')
        course['class_url'] = a_dict.get('class_url')
        course['image_labels'] = a_dict.get('image_labels')
        course['image_url'] = a_dict.get('image_url')
        course['project_title'] = a_dict.get('project_title')
        course['project_url'] = a_dict.get('project_url')
        list_dicts.append(course)

    response = json.dumps(list_dicts)
    
    return HttpResponse(response, content_type='text/json') 

def get_all_projects(request):
    '''
        Method that that returns all projects and its labels
        Parameters:
            request: HttpRequest Object
        Return:
            json with all projects and its labels
    '''
    if request.method == 'GET':
        all_projects = Project.objects.all()
        all_projects_dic ={}
        try:
            count = 0
            for project in all_projects:
                if count == 1000:
                    break
                images_list = []
                for img in project.image_set.all():
                    labels_list = []
                    for label in img.label_set.all():
                        labels_list.append({label.id: {
                            'label_name': label.label_name,
                            'label_confidence': label.label_confidence
                        }})
                        
                    images_list.append({img.id : {
                        'labels': labels_list,
                        'image_url': img.image_url
                    }})
                if len(images_list) != 0:
                    all_projects_dic[project.project_id] = {
                        'images': images_list,
                        'project_title': project.project_title,
                        'project_url': project.project_url,
                        'course': project.course.class_title,
                        'class_url': project.course.class_url,
                        'class_image': project.course.class_image 
                    }
                count += 1
            response = json.dumps(all_projects_dic)
        except:
            response = json.dumps([{'Error': 'No project in DataBase'}])
        return HttpResponse(response, content_type='text/json')  

def get_project(request, proj_id):
    '''
        Method that that receives a project id and it brings all projects images with 
        its labels.
        Parameters:
            request: HttpRequest Object
            proj_id (string): string that represents the project id
        Return:
            json with the project and its labels
    '''
    if request.method == 'GET':
        try:
            project = Project.objects.get(project_id=proj_id)
            project_dict ={}
            images_list = []
            for img in project.image_set.all():
                labels_list = []
                for label in img.label_set.all():
                    labels_list.append({label.id: {
                        'label_name': label.label_name,
                        'label_confidence': label.label_confidence
                    }})
                    
                images_list.append({img.id : {
                    'labels': labels_list,
                    'image_url': img.image_url
                }})
                
            project_dict[project.project_id] = {
                'images': images_list,
                'project_title': project.project_title,
                'project_url': project.project_url,
                'course': project.course.class_title
            }
            
                
            response = json.dumps(project_dict)
        except:
            response = json.dumps([{'Error': 'No project in DataBase'}])
        return HttpResponse(response, content_type='text/json')  
