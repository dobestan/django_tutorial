from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question)
    title = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)
