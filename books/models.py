from django.db import models
from django.contrib.auth.models import User
from djangotoolbox.fields import ListField, EmbeddedModelField, DictField
from django_mongodb_engine.contrib import MongoDBManager
import re

# BOOKS

class Text(models.Model):
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    editions = ListField(EmbeddedModelField('Edition'))
    slug = models.CharField(max_length=128)
    
    objects = MongoDBManager() 
    
    def __unicode__(self):
        return self.title
    
    def generateSlug(self):
        self.slug = re.sub('[^a-z0-9]+', '-', ('%s %s' % (self.author, self.title)).lower())
    
    def saveSlug(self):
        self.generateSlug()
        self.save()

class Edition(models.Model):
    published_date = models.DateField()
    publisher = models.CharField(max_length=128)
    books = ListField(EmbeddedModelField('Book'))

class Book(models.Model):
    condition = models.CharField(max_length=32, choices=(('New','New'), ('Used','Used'), ('Damaged','Damaged')), default='Used')
    notes = models.CharField(max_length=512)
    available = models.BooleanField(default=True)
        
# PEOPLE

class Person(models.Model):
    user = models.ForeignKey(User)
    tagline = models.CharField(max_length=1024)
    bio = models.TextField()
    collections = ListField(EmbeddedModelField('BookCollection'))

    def __unicode__(self):
        return self.user.get_full_name()

# COMMON

class BookCollection(models.Model):
    name = models.CharField(max_length=64)
    location = EmbeddedModelField('Location')
    books = ListField(models.ForeignKey(Book))
    
    def loadRecordList(self):
        self.records = self.getRecordList()
    
    def getRecordList(self):
        record_list = []
        for book_id in self.books:
            text = Text.objects.raw_query({'editions.books.id' : book_id })
            text = text[0]
            # edition = next(edition for edition in editions if book_id in (book['id'] for book in edition['books']))
            # book = next(book for book in edition['books'] if book['id'] == book_id)
            book_record = None
            for edition in text.editions:
                for book in edition.books:
                    if book.id == book_id:
                        book_record = {
                            'author' : text.author,
                            'title' : text.title,
                            'publisher' : edition.publisher,
                            'published_date' : edition.published_date,
                            'condition' : book.condition,
                            'notes' : book.notes,
                            'available' : book.available,
                            'book_id' : book.id,
                            'text_slug' : text.slug,
                        }
                        break
                if book_record is not None:
                    break
            if book_record is not None:
                record_list.append(book_record)
        return record_list

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
