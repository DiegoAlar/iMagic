#!/usr/bin/python3
"""
    Script that connects to AWS Elastic Search service and creates, or deletes and Index
"""
from elasticsearch import TransportError
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3
import json
import pprint
'''
#create index
bulk_file = ''
id = 1
with open('courses.json') as f:
    objs = json.load(f)
    for k, obj in objs.items():
        project_id = k
        project_title = obj.get('project_title')
        project_url = obj.get('project_url')
        course = obj.get('course')
        class_url = obj.get('class_url')
        class_image = obj.get('class_image')
        for imgs in obj.get('images'):
            for v in imgs.values():
                image_url = v.get('image_url')
                img_labels = {}
                for label in v.get('labels'):
                    for v in label.values():
                        if v.get('label_confidence') > 50:
                            img_labels[v.get('label_name')] = v.get('label_confidence')
        index = {
                'project_id': project_id,
                'class_url': class_url,
                'class_image': class_image,
                'project_title': project_title,
                'project_url': project_url,
                'course': course,
                'image_url': image_url,
                'image_labels': img_labels 
        }
        bulk_file += '{ "index" : { "_index" : "courses", "_type" : "_doc", "_id" : "' + str(id) + '" } }\n'
        bulk_file += json.dumps(index) + '\n'
        id += 1
'''
#end create index dict    
host = 'search-courses-4sagicofakcbjwqetzec5p7gs4.us-east-2.es.amazonaws.com' # For example, my-test-domain.us-east-1.es.amazonaws.com
region = 'us-east-2'
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service)
es = Elasticsearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection,
    timeout=120
    )
try:
    pass
    #es.indices.delete(index='courses', ignore=[400, 404]) # deletes an index
    #es.indices.create(index='courses', ignore=400) # creates an index
except TransportError as e:
    print(e.info)
#es.bulk(bulk_file) # You use this when you're creating the index and want to send the bulk with all the information needed
# print(bulk_file)
final_indices = es.indices.get_alias().keys()
print ("\nNew total:", len(final_indices), "indexes.")
for _index in final_indices:
    print ("Index name:", _index)
data = {
        "query": {
            "match" : {
                "project_id": 12620
        }
    }
}
pprint.pprint(es.search(data)) # To make a query in an Index

