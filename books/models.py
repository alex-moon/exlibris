from django.db import models
from people.models import Author, Person

class Publisher(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128) # TODO: address
    
    def __unicode__(self):
        return self.name + ', ' + self.location

class Text(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=512)
    
    def __unicode__(self):
        return self.title

class Edition(models.Model):
    text = models.ForeignKey(Text)
    published_date = models.DateField()
    publisher = models.ForeignKey(Publisher)
    # language = models.ForeignKey(Language)
    
    def __unicode__(self):
        return '%s (%s:%d)' % (self.text.title, self.publisher.name, self.published_date.year)

class Book(models.Model):
    edition = models.ForeignKey(Edition)
    owner = models.ForeignKey(Person)
    
    def _unicode__(self):
        return self.edition.text.title

