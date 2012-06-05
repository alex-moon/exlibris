from django.db import models
from django.contrib.auth.models import User
from djangotoolbox.fields import ListField, EmbeddedModelField, DictField
from django_mongodb_engine.contrib import MongoDBManager
import re

class Person(models.Model):
    user = models.ForeignKey(User)
    tagline = models.CharField(max_length=1024)
    bio = models.TextField()
    collections = ListField(EmbeddedModelField('BookCollection'))

    def __unicode__(self):
        return self.user.get_full_name()
        
class BookCollection(models.Model):
    name = models.CharField(max_length=64)
    location = EmbeddedModelField('Location')
    books = ListField(EmbeddedModelField('Book'))

class Book(models.Model):
    condition = models.CharField(max_length=32, choices=(('New','New'), ('Used','Used'), ('Damaged','Damaged')), default='Used')
    notes = models.CharField(max_length=512)
    available = models.BooleanField(default=True)
    edition = EmbeddedModelField('Edition')
    
class Edition(models.Model):
    published_date = models.DateField()
    publisher = models.CharField(max_length=128)
    text = EmbeddedModelField('Text')

class Text(models.Model):
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    
    objects = MongoDBManager()
    
    def __unicode__(self):
        return self.title
    
    def generateSlug(self):
        self.slug = re.sub('[^a-z0-9]+', '-', ('%s %s' % (self.author, self.title)).lower())
    
    def saveSlug(self):
        self.generateSlug()
        self.save()

class Location(models.Model):
    latlng = ListField()
    street = models.CharField(max_length=128)
    town = models.CharField(max_length=128)
    state = models.CharField(max_length=32)
    postcode = models.CharField(max_length=32)
    country = models.CharField(max_length=128)
    
    class MongoMeta:
        indexes = [{'fields': [('latlng', '2d')], 'min': -91, 'max': 91}]

    def __unicode__(self):
        return self.street + ' ' + self.town + (', ' + (self.state if self.state is not None else self.country) if self.state is not None and self.country is not None else '')
