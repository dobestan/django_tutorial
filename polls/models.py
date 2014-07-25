from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")
    def __unicode__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey(Question)
    title = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.title


"""
BEGIN;
CREATE TABLE "polls_question" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(100) NOT NULL,
    "pub_date" datetime NOT NULL
)
;
CREATE TABLE "polls_choice" (
    "id" integer NOT NULL PRIMARY KEY,
    "question_id" integer NOT NULL REFERENCES "polls_question" ("id"),
    "title" varchar(20) NOT NULL,
    "votes" integer NOT NULL
)
;

COMMIT;
"""
