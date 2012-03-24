from django.db import models

class Person(models.Model):
    tagline = models.CharField(max_length=1024)

class Author(models.Model):
    person = models.ForeignKey(Person)

