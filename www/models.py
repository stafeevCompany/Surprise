from django.db import models


class Answerss(models.Model):
    boolAnswer = models.BooleanField()

class Questionss(models.Model):
    text = models.TextField()

# Create your models here.
