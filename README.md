# Project Title

Skillshare/Rocket Team - iMagic

## Introduction

This is a POC done for Skillshare company, this product feature allows to find Skillshare courses related to an uploaded picture, this feature is thought for creative people who many times want to know how to replicate a specific piece of art but only a picture is what they can use to find what they want.

This software uses AWS Rekognition services to read images and determine the right labels for those, different types of services were explored, object and scene detection and Curtom Labels, finally, it was seen that a model trained with custom labels yielded better results as the courses recommended for a set of images were more relevant than those by using object and scene detection.

The software uses Elasticsearch from AWS to find the courses by given labels.

![alt text](https://github.com/skillshare-mentorship/holberton-image-recognition/blob/master/Classes_page.png?raw=true)


**Project Infrastructure**

![alt text](https://github.com/skillshare-mentorship/holberton-image-recognition/blob/master/Infrastructure.jpg?raw=true)

### There are four folders:
- **csv_files/files_csv:**
 This folder has a python script "aws_to_json.py" which is a script that reads aws credential from a CSV "access.csv" and also read information from two different CSV files from which images are extracted "holberton-skillshare-top-classes-projects.csv" and "holberton-skillshare-top-classes.csv", the images are sent to aws for Object and scene detection and then all the information about classes, projects and labels returned by aws are stored in a file "data.json" in JSON format. This scripts might be useful if it is desired to storage aws results in a JSON format, for the effect of the project, this script was used but a different approach was pursued later to store the information.
- **iMagic:**
This directory has the next.js application used to render the front-end pages, it has inside other three folder:
  - components:This folder has 2 Javascript files,  "Titles.js" which captures the input picture event, sends the picture to aws, receives the result of Rekognition, sends the results to Django API (To be explained later), receives the result from the API and then render dynamic content to the index page(To be explained later). The other file "Projects", captures an input which could be a project id or all and send a request to an API to render Skillshare projects with labels information.
  - pages:This older has the code to render the Courses(index.js) and Projects(projects.js) pages.
  - static:This folder has some pictures used in the page.
- **iMagic_python:**
This django folder has an API to serve classes information to be rendered in the front of the app and also it has a script to populate a DB with information regarding classes, projects and labels.
  - populate_DB.py: The first version of the script to populate the database, this version established a many to many relationships between courses and labels name. This DB design was unconsidered in the next steps.
  - courses_projects_to_DB.py(1), images_to_DB.py(2), labels_to_DB.py(3):Those scripts are a most recent version to populate the DB, this one includes a more complex DB design(Picture attached to this readme) and connects to aws to bring the label objects, to be successful at creating the DB with this scripts, those should be run in the same order they are listed here.
  - db.sqlite3:Please, review the DB Design below, the label objects were created using Curtom Labels.

       ![alt text](https://github.com/skillshare-mentorship/holberton-image-recognition/blob/master/database.jpg?raw=true)

  - my_app: Django app which has the API code, the file "models.py" has all the classes and relationships that correspond to tables in the database. The file "views.py" has the API methods used by the end-points. Most of the endpoints that were created initially are no longer in use and the methods used in the final app are  "get_course_titles_es" which connects with aws elastic search services and send it labels by a basic query, this method returns a JSON with the classes returned by Elasticsearch. The other two methods that the app is still using are "get_all_projects_es" and "get_project_by_id_es" which send a DSL query to Elasticsearch to receive the classes or class related to the given project.
  - iMagic_v1: this folder has in the file "settings.py" app configurations such as cors settings, it has also the file "urls.py" in which the end-points of the API are listed in urlpatterns.

- **others:**
This folder has the file "create_index_custom_lbs.py" which is the script used to create the last index in elastic search. It also has the file db.sqlite3 which is the database that contains the labels objects previously created with Object and Scene detection from AWS, this BD was not used in the final prototype but was kept for future references.

**Related links**

- [Link to the landing page] (https://diegoalar.github.io/Portfolio/)
- [Link to the deployed web-app] (http://18.209.104.186/)
- [LinkedIn Diego Alarcon] (https://www.linkedin.com/in/diego-andr%C3%A9s-alarcon-valencia-748442168/)
- [LinkedIn Mary Gomez] (https://www.linkedin.com/in/marylgomez/)
- [Link to project Blog] (https://medium.com/@mlgomez230/my-first-deep-learning-project-as-software-developer-ebb292616b52)


## Getting Started

To run this project in a local machine, it is required to have an AWS Access Key and AWS Secret Acess Key which can be introduced to a file with the name "access.csv" in the root of the first directory iMagic_v1. First-line 
YOUR_ACCESS_KEY and second-line YOUR_SECRET_ACCESS_KEY.
You can also set you credential as environmental variables or using aws like below:
```
$ aws configure
    AWS Access Key ID [None]: YOUR_ACCESS_KEY
    AWS Secret Access Key [None]: YOUR_SECRET_ACCESS_KEY
    Default region name [None]: your_region
    Default output format [None]: json
```

### Prerequisites

Django, Next.js, Python3


### Installing and running

Django Folder: iMagic_python

To better run the Django application, it is recommended to create a virtual environment and consider the following requirements.txt
```$ cat > requirements.txt```
```asgiref==3.2.3
attrs==19.3.0
awsebcli==3.18.1
bcrypt==3.1.7
blessed==1.17.6
boto3==1.13.19
botocore==1.15.49
cached-property==1.5.1
cement==2.8.2
certifi==2020.4.5.1
cffi==1.14.0
chardet==3.0.4
colorama==0.4.3
cryptography==2.9.2
Django==3.0.3
django-bootstrap4==1.1.1
django-cors-headers==3.3.0
django-crispy-forms==1.9.0
docker==4.2.1
docker-compose==1.25.5
dockerpty==0.4.1
docopt==0.6.2
docutils==0.15.2
elasticsearch==7.7.1
elasticsearch-dsl==7.2.1
future==0.16.0
idna==2.7
importlib-metadata==1.6.0
jmespath==0.10.0
jsonschema==3.2.0
mock==4.0.2
oauthlib==3.1.0
paramiko==2.7.1
pathspec==0.5.9
pbr==5.4.5
Pillow==7.0.0
pycparser==2.20
PyNaCl==1.4.0
pyrsistent==0.16.0
python-dateutil==2.8.0
pytz==2019.3
PyYAML==5.3.1
requests==2.20.1
requests-aws4auth==1.0
requests-oauthlib==1.3.0
s3transfer==0.3.3
semantic-version==2.5.0
six==1.11.0
soupsieve==2.0
sqlparse==0.3.0
termcolor==1.1.0
texttable==1.6.2
urllib3==1.24.3
wcwidth==0.1.9
websocket-client==0.57.0
zipp==3.1.0
```

```$ pip install -r requirements.txt```

Once everything is set, the server can be turned on as follows:
```
$ sudo python3 manage.py runserver
```

Next.js Folder: iMagic

```
$ npm init -y (initialize node project)
```
```
$ npm install next react react-dom
```

If issues are experienced by running the application:

```
$ npm cache clean --force
```
```
$ npm install
```
Once everyhintg is set, the server can be turned on as following:
```
$ sudo NEXT_PUBLIC_AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY NEXT_PUBLIC_AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY NEXT_PUBLIC_AWS_REGION=your_region npx next dev
```

 
## Authors
This Repository is written and mantained by **Mary Gomez** (1163@holbertonschool.com) and **Diego A. Alarcon** (1153@holbertonschool.com) 


## Acknowledgments
We would like to thank SkillShare for the opportunity to work on this awesome project, especially to Aaron Taylor for his valuable mentorship. Also, thanks to the academy Holberton for such a complete software development program.
