from django.db import models
from django.contrib.auth.models import User
from djangotoolbox.fields import ListField, EmbeddedModelField, DictField

# BOOKS

class Publisher(models.Model):
    name = models.CharField(max_length=128)
    locations = ListField(EmbeddedModelField('Location'))
    
    def __unicode__(self):
        return self.name + ', ' + self.location

class Text(models.Model):
    author = models.ForeignKey('Author')
    title = models.CharField(max_length=512)
    editions = ListField(EmbeddedModelField('Edition'))
    
    def __unicode__(self):
        return self.title

class Edition(models.Model):
    published_date = models.DateField()
    publisher = Publisher
    # language = models.ForeignKey(Language)
    books = ListField(EmbeddedModelField('Book'))
    
    def __unicode__(self):
        return '%s (%s:%d)' % (self.text.title, self.publisher.name, self.published_date.year)

class Book(models.Model):    
    def _unicode__(self):
        return self.edition.text.title
        
# PEOPLE

class Person(models.Model):
    user = models.ForeignKey(User)
    tagline = models.CharField(max_length=1024)
    collections = ListField(EmbeddedModelField('BookCollection'))

    def __unicode__(self):
        return self.user.get_full_name()

class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=128)
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
        
    def __unicode__(self):
        return self.get_full_name()

# COMMON

class BookCollection(models.Model):
    location = EmbeddedModelField('Location')
    books = ListField(Book)

class Location(models.Model):
    latlng = ListField()
    street = models.CharField(max_length=128)
    town = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    postcode = models.CharField(max_length=12)
    country = models.CharField(max_length=128)
    
    class MongoMeta:
        indexes = [{'fields': [('latlng', '2d')], 'min': -91, 'max': 91}]
        # check out Geospatial indexing
