from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.ForeignKey(User)
    tagline = models.CharField(max_length=1024)

class Author(models.Model):
    person = models.ForeignKey(Person)

