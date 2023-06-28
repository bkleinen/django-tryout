import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class BibTag(models.Model):
    name = models.CharField(max_length=50)
    

class Author(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=59)
 
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BibEntry(models.Model):
    class Meta:
        ordering = ["title"]
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=50)
    type = models.CharField(max_length=50) 
    pub_date = models.DateTimeField("date added")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(BibTag)
    
    def was_added_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.title


