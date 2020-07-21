from django.db import models

class Course(models.Model):
    '''
        All attributes are found in holberton-skillshare-top-classes.csv file
    '''
    class_title = models.CharField(max_length=100)
    class_url = models.CharField(max_length=100)
    class_sku = models.IntegerField(primary_key=True)
    class_image = models.CharField(max_length=100)

    class Meta:
        ordering = ['class_title']

class Label(models.Model):
    '''
        All attributes to create objects will be taken from AWS Rek response
    '''
    label_name = models.CharField(max_length=100)
    label_confidence = models.FloatField()
    #instances = models.TextField()  / This line to be included if it is desired to work with objects and scene detection
    #parents = models.TextField()    / This line to be included if it is desired to work with objects and scene detection
    image = models.ForeignKey(
        'Image',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['label_name']

class Image(models.Model):
    '''
        All attributes to create Image objects are taken from 
        holberton-skillshare-top-classes-projects.csv file
    '''
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
    )
    image_url = models.CharField(max_length=100)

    class Meta:
        ordering = ['image_url']

class Project(models.Model):
    '''
        All attributes to create Project objects are taken from 
        holberton-skillshare-top-classes-projects.csv file
    '''
    project_id = models.IntegerField(primary_key=True)
    project_title = models.CharField(max_length=100)
    project_url = models.CharField(max_length=100)
    course = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['project_title']
