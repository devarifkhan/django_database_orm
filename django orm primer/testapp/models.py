from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=100)
