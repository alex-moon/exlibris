from django.db import models
from people.models import Author, Person

class Text(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=512)
    # first_published = models.DateField

class Edition(models.Model):
    text = models.ForeignKey(Text)
    published_date = models.DateField()
    # publisher = models.ForeignKey(Publisher)
    # language = models.ForeignKey(Language)

class Book(models.Model):
    edition = models.ForeignKey(Edition)
    owner = models.ForeignKey(Person)

