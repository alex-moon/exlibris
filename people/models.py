from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.ForeignKey(User)
    tagline = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.user.get_full_name()

class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=128)
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
        
    def __unicode__(self):
        return self.get_full_name()
